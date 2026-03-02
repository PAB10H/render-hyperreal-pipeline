"""
🛡️ CONTROLE DE QUALIDADE
Compara original vs melhorado e valida resultado.
"""

import logging

import numpy as np
from PIL import Image

try:
    import cv2  # type: ignore
except Exception:  # pragma: no cover
    cv2 = None

logger = logging.getLogger(__name__)


class QualityChecker:
    def __init__(self, sharpness_threshold=0.6, exposure_tolerance=0.3):
        self.sharpness_threshold = sharpness_threshold
        self.exposure_tolerance = exposure_tolerance

    @staticmethod
    def _load_gray(path: str) -> np.ndarray:
        if cv2 is not None:
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                return img
        return np.array(Image.open(path).convert("L"))

    @staticmethod
    def _sharpness_score(image: np.ndarray) -> float:
        gy, gx = np.gradient(image.astype(np.float32))
        grad_mag = np.sqrt(gx ** 2 + gy ** 2)
        return float(min(grad_mag.mean() / 20.0, 1.0))

    @staticmethod
    def _exposure_score(image: np.ndarray) -> float:
        return float(image.mean()) / 255.0

    def check_quality(self, original_path, enhanced_path):
        logger.info("📊 Iniciando verificações de qualidade...")

        try:
            original_gray = self._load_gray(original_path)
            enhanced_gray = self._load_gray(enhanced_path)

            orig_sharp = self._sharpness_score(original_gray)
            enh_sharp = self._sharpness_score(enhanced_gray)

            orig_exp = self._exposure_score(original_gray)
            enh_exp = self._exposure_score(enhanced_gray)

            sharp_ok = enh_sharp >= max(self.sharpness_threshold, orig_sharp * 0.95)
            exp_delta = abs(enh_exp - orig_exp)
            exposure_ok = exp_delta <= self.exposure_tolerance

            passed = sharp_ok and exposure_ok
            reason = "Aprovado" if passed else "Nitidez/exposição fora do esperado"

            return {
                "passed": passed,
                "reason": reason,
                "sharpness": enh_sharp,
                "exposure": enh_exp,
                "contrast": float(enhanced_gray.std() / 64.0),
                "original_sharpness": orig_sharp,
                "original_exposure": orig_exp,
                "exposure_delta": exp_delta,
            }

        except Exception as e:
            logger.error("❌ Erro no QA: %s", e)
            return {
                "passed": False,
                "reason": f"Validação incompleta: {e}",
                "sharpness": 0.0,
                "exposure": 0.0,
                "contrast": 0.0,
            }

"""
🧠 ANALISADOR GPT
Gera análise técnica e prompt hiper-realista para render arquitetônico.
"""

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


class GPTAnalyzer:
    def __init__(self, gpt_link: str | None = None):
        self.gpt_link = gpt_link or os.getenv("GPT_ANALYZER_LINK", "https://chatgpt.com")

    def analyze_image(self, image_path: str):
        """Retorna uma análise técnica simulada para a imagem informada."""
        try:
            image = Path(image_path)
            logger.info("🧠 Iniciando análise técnica com GPT customizado...")
            logger.info("📤 Link: %s", self.gpt_link)

            return {
                "image_name": image.name,
                "realism_score": 7,
                "identified_problems": [
                    "Iluminação interna pouco natural",
                    "Texturas com baixa microvariação",
                    "Reflexos discretos em superfícies metálicas",
                ],
                "strengths": ["Composição equilibrada", "Boa perspectiva arquitetônica"],
                "hyperreal_prompt": (
                    "Transform this architectural render into a photorealistic interior photo, "
                    "with physically accurate global illumination, natural light bounce, "
                    "high-frequency texture detail in wood, concrete and fabrics, subtle lens "
                    "imperfections, cinematic dynamic range, realistic reflections and soft shadows, "
                    "maintaining the original composition and furniture layout."
                ),
            }
        except Exception as exc:
            logger.error("❌ Erro na análise da imagem: %s", exc)
            return None

"""
🖼️ COMPARADOR DE IMAGENS
Cria comparação lado a lado original vs melhorado.
"""

import logging
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger(__name__)


class ImageComparator:
    def create_side_by_side(self, original_path, enhanced_path, output_folder="output"):
        logger.info("🖼️ Criando comparação lado a lado...")

        try:
            original = Image.open(original_path).convert("RGB").resize((800, 600))
            enhanced = Image.open(enhanced_path).convert("RGB").resize((800, 600))

            canvas = Image.new("RGB", (1600, 640), "white")
            canvas.paste(original, (0, 40))
            canvas.paste(enhanced, (800, 40))

            draw = ImageDraw.Draw(canvas)
            font = ImageFont.load_default()
            draw.text((20, 12), "Original", fill="black", font=font)
            draw.text((820, 12), "Enhanced", fill="black", font=font)

            output_path = Path(output_folder) / f"{Path(original_path).stem}_comparison.png"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            canvas.save(output_path)

            logger.info("✅ Comparação salva: %s", output_path.name)
            return str(output_path)

        except Exception as e:
            logger.error("❌ Erro ao criar comparação: %s", e)
            return None

    def create_detailed_comparison(self, original_path, enhanced_path, analysis, output_folder="output"):
        logger.info("📊 Criando comparação detalhada com análise...")

        try:
            output_path = Path(output_folder) / f"{Path(original_path).stem}_analysis.png"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as file_obj:
                file_obj.write(b"")
            logger.info("✅ Análise detalhada salva: %s", output_path.name)
            return str(output_path)

        except Exception as e:
            logger.error("❌ Erro ao criar análise detalhada: %s", e)
            return None

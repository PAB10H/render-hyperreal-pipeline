"""
🖼️  COMPARADOR DE IMAGENS
Cria comparação lado a lado original vs melhorado
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class ImageComparator:
    def create_side_by_side(self, original_path, enhanced_path, output_folder="output"):
        logger.info("🖼️  Criando comparação lado a lado...")
        
        try:
            output_path = Path(output_folder) / f"{Path(original_path).stem}_comparison.png"
            logger.info(f"✅ Comparação salva: {output_path.name}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar comparação: {str(e)}")
            return None

    def create_detailed_comparison(self, original_path, enhanced_path, analysis, output_folder="output"):
        logger.info("📊 Criando comparação detalhada com análise...")
        
        try:
            output_path = Path(output_folder) / f"{Path(original_path).stem}_analysis.png"
            logger.info(f"✅ Análise detalhada salva: {output_path.name}")
            return str(output_path)
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar análise detalhada: {str(e)}")
            return None

"""
🎬 RENDER HYPERREAL PIPELINE — PROCESSAMENTO PROFISSIONAL
Pipeline sequencial de processamento de imagens de render com ChatGPT
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime
from gpt_analyzer import GPTAnalyzer
from image_generator import ImageGenerator
from quality_check import QualityChecker
from comparator import ImageComparator

# ===== CONFIGURAÇÃO DE LOGGING =====
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class RenderHyperrealPipeline:
    def __init__(self, input_folder="input", output_folder="output"):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.processed_folder = self.output_folder / "processed"
        self.comparisons_folder = self.output_folder / "comparisons"
        
        # Criar pastas se não existirem
        self.input_folder.mkdir(exist_ok=True)
        self.output_folder.mkdir(exist_ok=True)
        self.processed_folder.mkdir(exist_ok=True)
        self.comparisons_folder.mkdir(exist_ok=True)
        
        # Inicializar componentes
        self.analyzer = GPTAnalyzer()
        self.generator = ImageGenerator()
        self.quality_checker = QualityChecker()
        self.comparator = ImageComparator()
        
        logger.info("✅ Pipeline inicializado")

    def process_single_image(self, image_path, max_retries=3):
        logger.info(f"\n{'='*60}")
        logger.info(f"🖼️  PROCESSANDO: {image_path.name}")
        logger.info(f"{'='*60}")
        
        try:
            logger.info("[1/6] 🧠 Analisando imagem com GPT customizado...")
            analysis = self.analyzer.analyze_image(str(image_path))
            
            if not analysis:
                logger.error("❌ Falha na análise - abortando")
                return False
            
            logger.info(f"📊 Realism Score: {analysis.get('realism_score', 0)}/10")
            logger.info(f"🔍 Problemas identificados: {len(analysis.get('identified_problems', []))}")
            
            logger.info("[2/6] 📝 Gerando prompt hiper-realista avançado...")
            hyperreal_prompt = analysis.get('hyperreal_prompt', '')
            
            if not hyperreal_prompt:
                logger.error("❌ Falha ao gerar prompt - abortando")
                return False
            
            logger.info("[3/6] 🎨 Gerando imagem melhorada via ChatGPT Go...")
            attempt = 1
            enhanced_image_path = None
            
            while attempt <= max_retries:
                logger.info(f"   Tentativa {attempt}/{max_retries}...")
                enhanced_image_path = self.generator.generate_image(
                    image_path=str(image_path),
                    prompt=hyperreal_prompt,
                    output_folder=str(self.processed_folder)
                )
                
                if enhanced_image_path:
                    break
                attempt += 1
            
            if not enhanced_image_path:
                logger.error(f"❌ Falha ao gerar imagem após {max_retries} tentativas")
                return False
            
            logger.info(f"✅ Imagem gerada: {Path(enhanced_image_path).name}")
            
            logger.info("[4/6] 🛡️  Executando controle de qualidade...")
            quality_result = self.quality_checker.check_quality(
                original_path=str(image_path),
                enhanced_path=enhanced_image_path
            )
            
            if not quality_result['passed']:
                logger.warning(f"⚠️  Qualidade rejeitada: {quality_result['reason']}")
                logger.info("   Regenerando com prompt ajustado...")
                
                adjusted_prompt = self._adjust_prompt(hyperreal_prompt, quality_result)
                enhanced_image_path = self.generator.generate_image(
                    image_path=str(image_path),
                    prompt=adjusted_prompt,
                    output_folder=str(self.processed_folder)
                )
            else:
                logger.info(f"✅ Qualidade aprovada")
                logger.info(f"   Nitidez: {quality_result['sharpness']:.2f}")
                logger.info(f"   Exposição: {quality_result['exposure']:.2f}")
            
            logger.info("[5/6] 🖼️  Criando comparação side-by-side...")
            comparison_path = self.comparator.create_side_by_side(
                original_path=str(image_path),
                enhanced_path=enhanced_image_path,
                output_folder=str(self.comparisons_folder)
            )
            logger.info(f"✅ Comparação salva: {Path(comparison_path).name}")
            
            logger.info("[6/6] 📋 Salvando metadados...")
            metadata = {
                'timestamp': datetime.now().isoformat(),
                'original_file': image_path.name,
                'enhanced_file': Path(enhanced_image_path).name,
                'comparison_file': Path(comparison_path).name,
                'analysis': analysis,
                'quality_check': quality_result,
                'prompt_used': hyperreal_prompt
            }
            
            metadata_path = self.processed_folder / f"{image_path.stem}_metadata.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Metadados salvos: {metadata_path.name}")
            logger.info(f"\n{'='*60}")
            logger.info(f"✨ IMAGEM PROCESSADA COM SUCESSO!")
            logger.info(f"{'='*60}\n")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ ERRO ao processar imagem: {str(e)}", exc_info=True)
            return False

    def _adjust_prompt(self, original_prompt, quality_result):
        adjustments = []
        
        if quality_result['sharpness'] < 0.7:
            adjustments.append("aumentar nitidez e detalhe")
        
        if quality_result['exposure'] < 0.5:
            adjustments.append("aumentar exposição e brilho")
        elif quality_result['exposure'] > 1.5:
            adjustments.append("reduzir exposição, evitar overexposure")
        
        adjustment_text = ", ".join(adjustments)
        return f"{original_prompt}\n\n[Ajuste de qualidade: {adjustment_text}]"

    def process_folder(self):
        image_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.bmp'}
        image_files = [
            f for f in self.input_folder.iterdir()
            if f.suffix.lower() in image_extensions
        ]
        
        if not image_files:
            logger.warning("⚠️  Nenhuma imagem encontrada em /input")
            return
        
        logger.info(f"\n🚀 INICIANDO PROCESSAMENTO")
        logger.info(f"📁 Total de imagens: {len(image_files)}")
        logger.info(f"{'='*60}\n")
        
        successful = 0
        failed = 0
        
        for idx, image_path in enumerate(image_files, 1):
            logger.info(f"[{idx}/{len(image_files)}] Processando...")
            
            if self.process_single_image(image_path):
                successful += 1
            else:
                failed += 1
        
        logger.info(f"\n{'='*60}")
        logger.info(f"📊 RESUMO DO PROCESSAMENTO")
        logger.info(f"{'='*60}")
        logger.info(f"✅ Sucesso: {successful}")
        logger.info(f"❌ Falhas: {failed}")
        logger.info(f"📁 Resultados em: {self.output_folder}")
        logger.info(f"{'='*60}\n")

def main():
    pipeline = RenderHyperrealPipeline(
        input_folder="input",
        output_folder="output"
    )
    pipeline.process_folder()

if __name__ == "__main__":
    main()
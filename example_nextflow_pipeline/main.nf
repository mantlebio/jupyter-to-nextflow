include { PREPROCESS_IMAGES } from './modules/preprocessing'

log.info """\
    EXAMPLE PIPELINE
    ---------------------
    input_dir: ${params.input_dir}
    output_dir: ${params.output_dir}
"""
.stripIndent(true)

workflow {
    PREPROCESS_IMAGES ( params.input_dir, params.output_dir )
}
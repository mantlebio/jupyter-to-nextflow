process PREPROCESS_IMAGES {

    publishDir params.output_dir, mode: 'copy'
    
    input:
    path input_dir
    path output_dir

    output:
    path('*')

    script:
    """
    example_script.py \\
    ${input_dir} \\
    -o "./" \\
    """
}
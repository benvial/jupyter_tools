c = get_config()

c.Exporter.template_file = '/static/templates/slides.tpl'
c.TagRemovePreprocessor.remove_input_tags.add("rm_in")
c.TagRemovePreprocessor.remove_all_outputs_tags.add("rm_out")

c.SlidesExporter.reveal_theme="simple"

# the following does the equivalent of --no-prompt, see here: https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L109-L114
exporter_settings = {
    'exclude_input_prompt' : True,
    'exclude_output_prompt' : True,
}
c.TemplateExporter.update(exporter_settings)


# the following does the equivalent of --to slides and --post serve, see here: https://github.com/jupyter/nbconvert/blob/master/setup.py#L220 + https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L482 and here https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L238
# app_settings = {
#     "postprocessor_class": "nbconvert.postprocessors.serve.ServePostProcessor",
#     "export_format": "slides"
# }
# c.NbConvertApp.update(app_settings)
#
# server_settings = {
#     'ip' : "127.0.0.2",
#     'port' : 8001,
# }
#
# c.ServePostProcessor.update(server_settings)

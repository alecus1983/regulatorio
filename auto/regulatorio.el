(TeX-add-style-hook
 "regulatorio"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("book" "a5paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "paperwidth=15cm" "paperheight=20cm") ("inputenc" "utf8") ("fontenc" "T1") ("babel" "spanish" "es-tabla") ("biblatex" "backend=biber" "style=verbose" "hyperref=true") ("xcolor" "table" "dvipsnames") ("caption" "font=small" "labelfont=bf" "labelsep=endash")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "book"
    "bk10"
    "geometry"
    "inputenc"
    "fontenc"
    "babel"
    "amsmath"
    "amssymb"
    "graphicx"
    "acronym"
    "float"
    "mathpazo"
    "fancyhdr"
    "tikz"
    "tkz-tab"
    "easyReview"
    "tgbonum"
    "csquotes"
    "imakeidx"
    "biblatex"
    "longtable"
    "xcolor"
    "titling"
    "needspace"
    "hyperref"
    "tcolorbox"
    "empheq"
    "titlesec"
    "wasysym"
    "caption")
   (TeX-add-symbols
    '("chaptermark" 1))
   (LaTeX-add-labels
    "sec:tabladecontendos"
    "fig:planeamineto-operativo"
    "fig:aumentotension"
    "fig:reducciontension"
    "fig:edac"
    "fig:edac1"
    "fig:edac2"
    "fig:ens"
    "fig:insumoseventos"
    "fig:plazo1617"
    "fig:capacidad_conductores_emcali"
    "fig:ampacidad"
    "fig:eventogranmagnitud"
    "fig:reportes_transmision"
    "fig:mhaia"
    "fig:capacidad"
    "fig:mayor"
    "fig:esquema"
    "fig:excluidos"
    "fig:gruposcalidad"
    "fig:valoressaidi"
    "fig:tiporele"
    "fig:proteccionestrafo"
    "fig:diagramatrafo"
    "fig:diagramatrafo1"
    "fig:zonas_diferencial"
    "fig:tiposfusibles"
    "fig:prueba"
    "eq:1"
    "fig:lineaat"
    "fig:caso1"
    "fig:caso2"
    "fig:caso3"
    "fig:fasores"
    "fig:gd"
    "fig:polaridadtransformadores"
    "fig:paralelo"
    "tab:valorestierraretie"
    "fig:tnsystem"
    "fig:tttisystem"
    "fig:capacidaddeconductores"
    "fig:pruebas"
    "fig:protocoloscomunicacion"
    "fig:capa7iccp"
    "fig:iec61850"
    "fig:tipoproyecto"
    "fig:plazo646"
    "fig:trabajoadistancia"
    "fig:trabajocontacto"
    "fig:trabajoapotencial"
    "fig:sui"
    "fig:impacto")
   (LaTeX-add-bibliographies
    "bibliografia")
   (LaTeX-add-acronyms
    "CND"
    "COMTRADE"
    "DNA"
    "EDAC"
    "ENS"
    "FMECA"
    "FNCER"
    "LAC"
    "OR"
    "PENS"
    "RCM"
    "RETIE"
    "SAEB"
    "SDL"
    "SIN"
    "SP"
    "STN"
    "STR"
    "SOE"
    "UPME")
   (LaTeX-add-xcolor-definecolors
    "enlace"
    "titleblue"
    "titlegreen")
   (LaTeX-add-tcolorbox-tcbuselibraries
    "skins,breakable,listings,theorems"))
 :latex)


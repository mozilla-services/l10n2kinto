for lang in af ar as ast az be bg bn_BD bn_IN bs ca cs cy da de dsb el en_GB eo es-AR es-CL es-ES es-MX et eu fa ff fi fr fy fy_NL ga gd gl gu_IN he hi_IN hr hsb ht hu hy_AM id it ja kk km kn ko ku lij lt lv mk ml mn ms my nb_NO ne_NP nl or pa pa_IN pl pt pt_BR pt_PT rm ro ru si sk sl son sq sr sv_SE ta te th tr uk ur vi xh zh_CN zh_TW zu
do 
  echo "Starting with $lang"
  l10n2kinto -v -s https://kinto-ota.dev.mozaws.net/v1 \
                -b loop-client -c "$lang" -u mark:p4ssword \
                ../loop-client-l10n/l10n/$lang/*.properties || exit 1
done

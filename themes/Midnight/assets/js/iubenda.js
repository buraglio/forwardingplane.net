{{- if and (not $.Site.IsServer) (and $.Site.Params.iubenda.pro.enable_cookie_policy (and $.Site.Params.iubenda.id $.Site.Params.iubenda.pro.site_id)) -}}
{{- $url := urls.Parse $.Site.BaseURL -}}
var _iub = _iub || [];
_iub.csConfiguration = {
    cookiePolicyId: {{ $.Site.Params.iubenda.id }},
    siteId: {{ $.Site.Params.iubenda.pro.site_id }},
    lang: "en",
    consentOnScroll: true,
    localConsentPath: {{ $url.Path }}
    {{- if not $.Site.Params.iubenda.pro.prior_consent }},
    priorConsent: false,
    {{- end }},
    banner: {
        slideDown: false,
        applyStyles: false,
        content: "<p>{{ i18n "cookie_banner" }}</p>"
    }
};
{{- end -}}

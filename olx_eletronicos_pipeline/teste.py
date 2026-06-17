from curl_cffi import requests
from bs4 import BeautifulSoup as bs

sessao = requests.Session(impersonate="chrome")

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'pt-BR,pt;q=0.7',
    'Connection': 'keep-alive',
    'referer': 'https://pe.olx.com.br/',
    'cookie': 'r_id=0cc932e8-2150-4fa4-8d4f-d51940c40e7b; _cfuvid=BC5h8NfM7tL2oKQ1HZJiJhNbDXROHwyl3_LJaJSrBPA-1781696631.4458797-1.0.1.1-z3s4cgCvfKzJGsksucCcTgjzeHj28ZXKHTG2t6NC43M; nl_id=630fecbe-515e-4b7b-a788-883587b223bd; l_id=ef21ddc0-9948-4c96-ab2b-191096f6efd1; cf_clearance=Ne3L.ONVvVtd93YeL1H9y2jMPa3tqg7CYW9GXYUCnvE-1781702036-1.2.1.1-gll_U0lWjreD8QDG1pr2Ze8StXVqUDDcLL.eqoD7R6fsaoTB3JsXLQbt1rrlFbFuqeMYBDBPz4eQlHsY3FXKgmPkyeFPUXjiRf1KVRqFxYswYEozIVIpghYncFQFRi9mjOyVzfHnJvJ2fAjl7QkmaWZprxIjUgVsw.lNhg8GsTh9eTejCIti0AcWVDCWEtL3NCff3btP_n2cmkqAacAhXpgCGWqlEJB2WDfg7YBkwUqvSvSrdUUeXnEQ6byNpGEcspkRQ7QPXjbCOZIBHlaK3.xPXgEWjuYZ6pZxS8ta1_se6nF7vc2nP63SI98qEE6LNECZJ56PnWSQ5lhYmENONg; adview-onboarding-date-to-see-again=2026-06-20T13:15:28.224Z; TestAB_Groups=sanityweb50_control.payg-discount-re-julius_ml-ranges.dpd-aiout_enabled.ln-redchat_A.palq-1528_enabled.imo-92fed3_enabled.imo-514362_enabled.lp85_control.rp-bsc-off_enabled.lp199_enabled.lp204_control.topovip_enabled.stempesp_enabled.cht-report_enabled.submit-bfr_enabled.switch-seg_enabled.bcnNewCard_enabled.rec-8584e_enabled.sxp-hexa_enabled.rec-f7f1ca_enabled.log-rdsgn_control.adview-ecg_enabled.bjTPZ-np-w_b.sa-fgp-dlv_enabled.lp436_A.acc-iv-nd_enabled.autos-prc2_enabled.nutps_b.sxp-dedup_enabled.rep-newrp_enabled.lp503_A.ne-video3_control.ne-video4_control.ne-video5_control.ne-video6_A.bjTPZ-ocsd_enabled.ai-cat-mod_enabled.ne-pdf2_A.rec-wb41aa_enabled.bcnExitInt_control.bcnWaGal_enabled.ne-pdf3_control.bjTPZ-rpo_b.ne-pdf4_control.ne-pdf5_control.ne-pdf6_control.had-ch28c3_enabled.dpd-sv-od_control.rep-sv-lgn_control; __cf_bm=oW9N1z7EpRLFOw1r5H2hpoxADhO56gge_8k.cOn_ELY-1781704671.9870417-1.0.1.1-24VpUkqpU_mhas6MG5OPlbRPHbn9Wbg1W6y2KlWJukuyu6bgjVoxL2BkeS7UN79JiH7RbDqS0SnpxMs3UIQqWO2U93A4z9j1yTRqRloUZaWPIvgNc18GAhEQEIPVlaus'
}

sessao.headers.update(header)

url = "https://pe.olx.com.br/grande-recife/celulares/celular-iphone-14-plus-128gb-em-perfeito-estado-87-1508820428?lis=listing_3060"
requisicao = sessao.get(url)

print(requisicao)  

site = bs(requisicao.text, "html.parser")
print(site.prettify())
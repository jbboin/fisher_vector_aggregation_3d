# Script modified from Python downloader script at:
# http://redwood-data.org/3dscan/dataset.html?c=sculpture

########################################################
# Python script for downloading RGB-D sequences
# - tested with Python 2.7 or 3.x
# - this script requires 'requests' module
# For more details, visit http://redwood-data.org/3dscan
########################################################

import config
import requests, os

def download_file_from_google_drive(id, dest_dir, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, os.path.join(dest_dir, destination))

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

dest_dir = os.path.join(config.DATASET_DIR, 'model_zip')
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

print('Dowloading dataset : sculpture, sequence id : 01312')
download_file_from_google_drive('1k0fDM_Xtni5YAnz4APaFn_2CUllRxLi5', dest_dir, '01312.zip')

print('Dowloading dataset : sculpture, sequence id : 01324')
download_file_from_google_drive('1XCz7n1O8AEkhwZiw34KYlycU3HTQjBsg', dest_dir, '01324.zip')

print('Dowloading dataset : sculpture, sequence id : 01325')
download_file_from_google_drive('18VjfYS_8ociA-p0-OT6BOv39M232d-JE', dest_dir, '01325.zip')

print('Dowloading dataset : sculpture, sequence id : 01326')
download_file_from_google_drive('1bWk_vzKBQGPQQuBr-MTZw3yFu5mgKZNP', dest_dir, '01326.zip')

print('Dowloading dataset : sculpture, sequence id : 01327')
download_file_from_google_drive('1WTzE389rsdisvzsx1C0R52wTn2nqj46J', dest_dir, '01327.zip')

print('Dowloading dataset : sculpture, sequence id : 01328')
download_file_from_google_drive('16g-9owb27XroXqc0E61_h0GfBW2HSbiR', dest_dir, '01328.zip')

print('Dowloading dataset : sculpture, sequence id : 01329')
download_file_from_google_drive('1dAihaZuioK3hxsn13rWROY1hC2tkVj5g', dest_dir, '01329.zip')

print('Dowloading dataset : sculpture, sequence id : 01332')
download_file_from_google_drive('19RFFUQK9M6H7q4MASsK87uFU6OXtxzCS', dest_dir, '01332.zip')

print('Dowloading dataset : sculpture, sequence id : 01831')
download_file_from_google_drive('1gb4b6umD4acdYmQdb3WtX7b5SQJ3GX6h', dest_dir, '01831.zip')

print('Dowloading dataset : sculpture, sequence id : 01834')
download_file_from_google_drive('1kWf1WZ2Ln1LU5kg7vh7Tkaz1PVbmyq0k', dest_dir, '01834.zip')

print('Dowloading dataset : sculpture, sequence id : 01835')
download_file_from_google_drive('1xx-hnc2Y8NA_U6DaMFfOikqURojEuRnU', dest_dir, '01835.zip')

print('Dowloading dataset : sculpture, sequence id : 01836')
download_file_from_google_drive('1cSHAv5ONLC_oyfTICpz1kYuTzwMzRAgz', dest_dir, '01836.zip')

print('Dowloading dataset : sculpture, sequence id : 01837')
download_file_from_google_drive('1_mxl9Ze7yQIfSYA0SkUEYq-bmSmc7cwK', dest_dir, '01837.zip')

print('Dowloading dataset : sculpture, sequence id : 01838')
download_file_from_google_drive('1q32lQuStJdNXGSw8hVwKDw_nZBIEGkdo', dest_dir, '01838.zip')

print('Dowloading dataset : sculpture, sequence id : 01859')
download_file_from_google_drive('1FSLB6ROYnmIKClj-zRJcROLWjYxlxmEM', dest_dir, '01859.zip')

print('Dowloading dataset : sculpture, sequence id : 01860')
download_file_from_google_drive('1Xq7dmWDtGk6mnPsFOUkB3tNR70zzedDa', dest_dir, '01860.zip')

print('Dowloading dataset : sculpture, sequence id : 01861')
download_file_from_google_drive('1Dh_ZmnX970RkVZ0EksO62x6XAF0_HntD', dest_dir, '01861.zip')

print('Dowloading dataset : sculpture, sequence id : 01869')
download_file_from_google_drive('10svam_2PPyaq6ERUgRu1wgd-WFRI9s8S', dest_dir, '01869.zip')

print('Dowloading dataset : sculpture, sequence id : 01870')
download_file_from_google_drive('1oGvsuTzmlJKPfmxG6-1v0QrSHWChRuPv', dest_dir, '01870.zip')

print('Dowloading dataset : sculpture, sequence id : 01871')
download_file_from_google_drive('18BQlHo9bUDncWdEzhG6Nn11QO9RYMMTd', dest_dir, '01871.zip')

print('Dowloading dataset : sculpture, sequence id : 01872')
download_file_from_google_drive('1mu_81GbPz-CvabjQuqXSQf-8FejU5cBL', dest_dir, '01872.zip')

print('Dowloading dataset : sculpture, sequence id : 01873')
download_file_from_google_drive('1f7dldcYJEFro0MVzkgq6w8FM27DYyGHX', dest_dir, '01873.zip')

print('Dowloading dataset : sculpture, sequence id : 01875')
download_file_from_google_drive('1C9wbPpnyN1UsJsgjAj4T8DPLQLgyEO0E', dest_dir, '01875.zip')

print('Dowloading dataset : sculpture, sequence id : 01876')
download_file_from_google_drive('1n6GBe7JMh8hRSXhOYFaIs2EHhLLRYs3l', dest_dir, '01876.zip')

print('Dowloading dataset : sculpture, sequence id : 01877')
download_file_from_google_drive('1A3L8A4GpTxhg67qT9Lh7rzOl2oOj0xK9', dest_dir, '01877.zip')

print('Dowloading dataset : sculpture, sequence id : 01878')
download_file_from_google_drive('1HmEb14nXJdY9GidgT2D7qOuItl6UXoe-', dest_dir, '01878.zip')

print('Dowloading dataset : sculpture, sequence id : 01879')
download_file_from_google_drive('1LcsZ9PtDa8LU5GScigB-aaUR26r224Pj', dest_dir, '01879.zip')

print('Dowloading dataset : sculpture, sequence id : 01880')
download_file_from_google_drive('1YCwMqmkK0s6osAP6pye46t00A5ykiysm', dest_dir, '01880.zip')

print('Dowloading dataset : sculpture, sequence id : 01881')
download_file_from_google_drive('1s_TgwjD9Y3a0pw3fLFAxp5qgj5RFI8NA', dest_dir, '01881.zip')

print('Dowloading dataset : sculpture, sequence id : 01882')
download_file_from_google_drive('14tvwcORUgh79EO3F2Y_xKMFMxTZ-0UII', dest_dir, '01882.zip')

print('Dowloading dataset : sculpture, sequence id : 01883')
download_file_from_google_drive('1npLOPK-shjxJFBV6qzrYsy4Lhx7Nt7KB', dest_dir, '01883.zip')

print('Dowloading dataset : sculpture, sequence id : 01885')
download_file_from_google_drive('1lQswiYBACfb1Cb2voQArWTxhMAMsEVxV', dest_dir, '01885.zip')

print('Dowloading dataset : sculpture, sequence id : 01886')
download_file_from_google_drive('1m_GLRsWeMgKjGMyZ7y8ZlM93n85NvdAp', dest_dir, '01886.zip')

print('Dowloading dataset : sculpture, sequence id : 01887')
download_file_from_google_drive('1GCfh3DHffAX9QSkrLpmVk5L6nuQK57dO', dest_dir, '01887.zip')

print('Dowloading dataset : sculpture, sequence id : 02159')
download_file_from_google_drive('14opl7UkszqycaMOpeumcLTxMGc_1GsJw', dest_dir, '02159.zip')

print('Dowloading dataset : sculpture, sequence id : 02172')
download_file_from_google_drive('17xxC8ZujSe1Cp9j0zu4gzsE2FymG1Aw9', dest_dir, '02172.zip')

print('Dowloading dataset : sculpture, sequence id : 02174')
download_file_from_google_drive('1AD_DZpWjEfGqXdDYyreqDh5cnallbWo-', dest_dir, '02174.zip')

print('Dowloading dataset : sculpture, sequence id : 02315')
download_file_from_google_drive('1nnQlmsgaHlimuz283Bw7IExVuhiM3YNk', dest_dir, '02315.zip')

print('Dowloading dataset : sculpture, sequence id : 02326')
download_file_from_google_drive('1qp-F0-gumKXNgM78sBUeK1wnEiTgT3MY', dest_dir, '02326.zip')

print('Dowloading dataset : sculpture, sequence id : 02378')
download_file_from_google_drive('1WSGhHuCKB3_BuPIfqfMjN6b8V1KFMlOu', dest_dir, '02378.zip')

print('Dowloading dataset : sculpture, sequence id : 02543')
download_file_from_google_drive('1GTA_Cpq89C6f4iIUNAV1OqUWAb99iHGw', dest_dir, '02543.zip')

print('Dowloading dataset : sculpture, sequence id : 02654')
download_file_from_google_drive('1hxiG7umTqJ9_iG0swA6SlA87Mt028pnR', dest_dir, '02654.zip')

print('Dowloading dataset : sculpture, sequence id : 02656')
download_file_from_google_drive('1qgYnNHzYPiJlWO9E463IcZwIl-2d9dF9', dest_dir, '02656.zip')

print('Dowloading dataset : sculpture, sequence id : 02658')
download_file_from_google_drive('1ZkFrb_ukkX5mwSeHRU7D0-tiBP_MeTgG', dest_dir, '02658.zip')

print('Dowloading dataset : sculpture, sequence id : 02669')
download_file_from_google_drive('10FhJAi450zNyivvQFHe_cxiFgDOl_fC8', dest_dir, '02669.zip')

print('Dowloading dataset : sculpture, sequence id : 02670')
download_file_from_google_drive('1HhvTx_d1Va24h4ZVjBl6Uy2HF0I4rjhi', dest_dir, '02670.zip')

print('Dowloading dataset : sculpture, sequence id : 02690')
download_file_from_google_drive('1nmSEEJLwahux5LhTHuw4V4mT52vBOSuw', dest_dir, '02690.zip')

print('Dowloading dataset : sculpture, sequence id : 02700')
download_file_from_google_drive('1DlchkSmg8HAZ-bP1hBlw5_tlfhKYz3w8', dest_dir, '02700.zip')

print('Dowloading dataset : sculpture, sequence id : 02706')
download_file_from_google_drive('1iCQDGDlac1ZlD8ubBZAECfF9X-NT5kkx', dest_dir, '02706.zip')

print('Dowloading dataset : sculpture, sequence id : 02732')
download_file_from_google_drive('14dGbrQRMOxshkBWfmf427vdgN7BXxj5S', dest_dir, '02732.zip')

print('Dowloading dataset : sculpture, sequence id : 02737')
download_file_from_google_drive('1XBUEznMQvQVn_PLS_r5DZeVWr-eSgs4E', dest_dir, '02737.zip')

print('Dowloading dataset : sculpture, sequence id : 02738')
download_file_from_google_drive('1U8tt4vGQTVcKl8XQsbyEXdB7F4EGs1rT', dest_dir, '02738.zip')

print('Dowloading dataset : sculpture, sequence id : 02740')
download_file_from_google_drive('1RoIMu4bpfuGQoHH2Ic4GzUHZF12fbxkG', dest_dir, '02740.zip')

print('Dowloading dataset : sculpture, sequence id : 02743')
download_file_from_google_drive('1bSbbjrfHD5P5RB7u2KFQC9SGvkDVqqm5', dest_dir, '02743.zip')

print('Dowloading dataset : sculpture, sequence id : 02780')
download_file_from_google_drive('1A2OYRJwtMXCOiLuGBjBTJaFKWims7SjT', dest_dir, '02780.zip')

print('Dowloading dataset : sculpture, sequence id : 02789')
download_file_from_google_drive('1sk2I7l6hr3Q3gRYuLBGFx5croPBwN2Xx', dest_dir, '02789.zip')

print('Dowloading dataset : sculpture, sequence id : 02801')
download_file_from_google_drive('1TBIKF3Dg_BjEEG1pnNLdJPdtxOX_GFhZ', dest_dir, '02801.zip')

print('Dowloading dataset : sculpture, sequence id : 02821')
download_file_from_google_drive('1KkETT5U9izB6YDgFeGOKC36j7L4MNCIt', dest_dir, '02821.zip')

print('Dowloading dataset : sculpture, sequence id : 02823')
download_file_from_google_drive('1JtxF-peeOoePGAoitTE_S0DJwr8recJd', dest_dir, '02823.zip')

print('Dowloading dataset : sculpture, sequence id : 02852')
download_file_from_google_drive('1V8ibyzVELh0Xevygm2A3MA1_MmGkEC5U', dest_dir, '02852.zip')

print('Dowloading dataset : sculpture, sequence id : 02853')
download_file_from_google_drive('1i6_sW-98a2vUP17vS7C9DlwTlJllYhzt', dest_dir, '02853.zip')

print('Dowloading dataset : sculpture, sequence id : 02854')
download_file_from_google_drive('1GizAolnfMv7UVgUQSKw0JCxCC8M-3uzG', dest_dir, '02854.zip')

print('Dowloading dataset : sculpture, sequence id : 02855')
download_file_from_google_drive('1kSpLIAtdcK6ee-cq0AbtahTHLSqqiXFx', dest_dir, '02855.zip')

print('Dowloading dataset : sculpture, sequence id : 02856')
download_file_from_google_drive('1qAYIJ9WOURqD8uAqmgElxu4C1TGW04sc', dest_dir, '02856.zip')

print('Dowloading dataset : sculpture, sequence id : 02858')
download_file_from_google_drive('1z1CjOBLpQCh9YD1o7iFKDtv8lhpNsKN9', dest_dir, '02858.zip')

print('Dowloading dataset : sculpture, sequence id : 02859')
download_file_from_google_drive('1e2swHz2fddCkJy0hWlTqhqmyP0_CTGDb', dest_dir, '02859.zip')

print('Dowloading dataset : sculpture, sequence id : 02861')
download_file_from_google_drive('1RJEuH0Y79H__WHZ4fy90VDtLCrF8Geye', dest_dir, '02861.zip')

print('Dowloading dataset : sculpture, sequence id : 03008')
download_file_from_google_drive('1xBoSnxi_aKnTA-MHMn7BRWd0iW7VfC7W', dest_dir, '03008.zip')

print('Dowloading dataset : sculpture, sequence id : 03021')
download_file_from_google_drive('1VTPLftY6JoCeUWsLmgVtz-VvsYJHUKhO', dest_dir, '03021.zip')

print('Dowloading dataset : sculpture, sequence id : 03027')
download_file_from_google_drive('1FYVbBfwrfuE2fIiOSkvQ1jqcmEpsgf-j', dest_dir, '03027.zip')

print('Dowloading dataset : sculpture, sequence id : 03038')
download_file_from_google_drive('1psAnj45MelwZeufT6Rx5DaExUHKWKS9u', dest_dir, '03038.zip')

print('Dowloading dataset : sculpture, sequence id : 03043')
download_file_from_google_drive('1wCJksbo9Jjy1n3hcTpLJ5GA71bgmSJD_', dest_dir, '03043.zip')

print('Dowloading dataset : sculpture, sequence id : 03044')
download_file_from_google_drive('1lqNMwl68VdY94Ykgh8Tj7uchuKxaYs7T', dest_dir, '03044.zip')

print('Dowloading dataset : sculpture, sequence id : 03046')
download_file_from_google_drive('1uPMF82nUNhCX1xzbqDMe2Lj98rBYtvEz', dest_dir, '03046.zip')

print('Dowloading dataset : sculpture, sequence id : 03047')
download_file_from_google_drive('1Y7m_50rukNaSXRXo9GvQn3GMD3EwMrk8', dest_dir, '03047.zip')

print('Dowloading dataset : sculpture, sequence id : 03133')
download_file_from_google_drive('127qcAB1KxexBIx4sNmxWiiVYIbJDMEsA', dest_dir, '03133.zip')

print('Dowloading dataset : sculpture, sequence id : 03147')
download_file_from_google_drive('1p88cDHK4GxmPUO3MDIs-hse63LpuKEIx', dest_dir, '03147.zip')

print('Dowloading dataset : sculpture, sequence id : 03148')
download_file_from_google_drive('1Y0A7VwQi1csctQl820ipuyAxfRlipWPY', dest_dir, '03148.zip')

print('Dowloading dataset : sculpture, sequence id : 03197')
download_file_from_google_drive('1ITbKH_zflWfsz_DPtrWpEYO3zzJFCVgE', dest_dir, '03197.zip')

print('Dowloading dataset : sculpture, sequence id : 03198')
download_file_from_google_drive('1_f79CTFFcphLDXmR0cai-62uMyhMtPhw', dest_dir, '03198.zip')

print('Dowloading dataset : sculpture, sequence id : 03212')
download_file_from_google_drive('1dYJd7P2zzpzBHqjXVkieF-8dYiALevQy', dest_dir, '03212.zip')

print('Dowloading dataset : sculpture, sequence id : 03218')
download_file_from_google_drive('1ergxZecOvJJ9WQ86y8bmbx4MSROF-N_W', dest_dir, '03218.zip')

print('Dowloading dataset : sculpture, sequence id : 03221')
download_file_from_google_drive('1KMUITWl52a9K25iFMOpC9e6rspllyzIC', dest_dir, '03221.zip')

print('Dowloading dataset : sculpture, sequence id : 03222')
download_file_from_google_drive('1VzohIQpXRXTjXnPkB4SBj8QmXmZvWYsi', dest_dir, '03222.zip')

print('Dowloading dataset : sculpture, sequence id : 03232')
download_file_from_google_drive('1pIRcXFsp4PFzvMbIsmT7tHOb-D5ix2C-', dest_dir, '03232.zip')

print('Dowloading dataset : sculpture, sequence id : 03238')
download_file_from_google_drive('1leJj3fTpEqUl3tZYbTA5N_Dzndo2Uwrf', dest_dir, '03238.zip')

print('Dowloading dataset : sculpture, sequence id : 03243')
download_file_from_google_drive('1xqgTbbanLKn-SP7DkUgEQG2fxw0_dIFx', dest_dir, '03243.zip')

print('Dowloading dataset : sculpture, sequence id : 03253')
download_file_from_google_drive('1PWeLpNRXCflPI98CBj6N4fSiaER0Fio6', dest_dir, '03253.zip')

print('Dowloading dataset : sculpture, sequence id : 03258')
download_file_from_google_drive('1F8ZnkoWsU4V8IuM3WCfnB1TgcVa3_D8H', dest_dir, '03258.zip')

print('Dowloading dataset : sculpture, sequence id : 03259')
download_file_from_google_drive('16ItuaksvRDbVnnvQfJA1doX56Gv2wtMU', dest_dir, '03259.zip')

print('Dowloading dataset : sculpture, sequence id : 03262')
download_file_from_google_drive('1pT77s7-avG9SjOp1tV1nJkpnRZYn0llM', dest_dir, '03262.zip')

print('Dowloading dataset : sculpture, sequence id : 03263')
download_file_from_google_drive('1s3zzep_HvUuUdM6n_USsw-vmpFlo31ci', dest_dir, '03263.zip')

print('Dowloading dataset : sculpture, sequence id : 03478')
download_file_from_google_drive('1RGHsrqguWhMVZy4Ga7A6im4eV7po0S2t', dest_dir, '03478.zip')

print('Dowloading dataset : sculpture, sequence id : 03519')
download_file_from_google_drive('1Ej8utec-mWUoCPEj7cGqZsaAPr86XuBu', dest_dir, '03519.zip')

print('Dowloading dataset : sculpture, sequence id : 03529')
download_file_from_google_drive('1UWcMlbT3nPrPZLMDQJEDKyf6jbYA2YBb', dest_dir, '03529.zip')

print('Dowloading dataset : sculpture, sequence id : 03553')
download_file_from_google_drive('1atcFKSJ8Eig91dZKaJTq-m1J_BH_9K5R', dest_dir, '03553.zip')

print('Dowloading dataset : sculpture, sequence id : 03566')
download_file_from_google_drive('1icmK7ObzxcOKOBOQAlFMbtEmOqiznIO8', dest_dir, '03566.zip')

print('Dowloading dataset : sculpture, sequence id : 03591')
download_file_from_google_drive('1GaMRRp7nuzZNuN4rRTKQNaRi39My_aa-', dest_dir, '03591.zip')

print('Dowloading dataset : sculpture, sequence id : 03592')
download_file_from_google_drive('1QE3K_jJ9SDlLyOIZAieAF5u61K7QR2A3', dest_dir, '03592.zip')

print('Dowloading dataset : sculpture, sequence id : 03717')
download_file_from_google_drive('1rF4ykFT-d4ZSotbmYSe_hh4LmogW-lHb', dest_dir, '03717.zip')

print('Dowloading dataset : sculpture, sequence id : 03718')
download_file_from_google_drive('1NVSQx-OQ42bz_Lx5YJmJFP3EKr2AcWfV', dest_dir, '03718.zip')

print('Dowloading dataset : sculpture, sequence id : 03719')
download_file_from_google_drive('19-o8oy9mdQ-L7adL8k9RD_Rz6p3MbIfr', dest_dir, '03719.zip')

print('Dowloading dataset : sculpture, sequence id : 03720')
download_file_from_google_drive('1s6dveyLRyeW-_LdwpQsIRc5WaIUVOmEE', dest_dir, '03720.zip')

print('Dowloading dataset : sculpture, sequence id : 03721')
download_file_from_google_drive('1dW-joZ1PcFIDuW2Qdd0lpk7DlmibIwyN', dest_dir, '03721.zip')

print('Dowloading dataset : sculpture, sequence id : 03722')
download_file_from_google_drive('1lAVvVzillVN5Y7miaQs6ikYpu_G6ZVaa', dest_dir, '03722.zip')

print('Dowloading dataset : sculpture, sequence id : 03723')
download_file_from_google_drive('1eEFifNScXiatHZDRQTSdVsX26d1hdRox', dest_dir, '03723.zip')

print('Dowloading dataset : sculpture, sequence id : 03724')
download_file_from_google_drive('1JFq03VZJDfGLiN8_JgfMcKI2nWUc-ltV', dest_dir, '03724.zip')

print('Dowloading dataset : sculpture, sequence id : 03725')
download_file_from_google_drive('1Y5YPr0lZmKG_xbqeKmVe6_M8gjmNFjCK', dest_dir, '03725.zip')

print('Dowloading dataset : sculpture, sequence id : 03726')
download_file_from_google_drive('1EOVvL3dWiFevyl6PjRn_jd2fw-Sobi0K', dest_dir, '03726.zip')

print('Dowloading dataset : sculpture, sequence id : 03727')
download_file_from_google_drive('1Iw4SAGvkFx8WFlshwnRs8zFLky9kASN2', dest_dir, '03727.zip')

print('Dowloading dataset : sculpture, sequence id : 03728')
download_file_from_google_drive('1rlM99YhIgujQgjIkR0wvuGw-cI9M8WvR', dest_dir, '03728.zip')

print('Dowloading dataset : sculpture, sequence id : 03729')
download_file_from_google_drive('1TJuClNqgNN4pfRzqmaN8iRaBwly4UDk5', dest_dir, '03729.zip')

print('Dowloading dataset : sculpture, sequence id : 03850')
download_file_from_google_drive('1PmKLtG7FYREo6eN3XFnWD7AYhYC5VdE2', dest_dir, '03850.zip')

print('Dowloading dataset : sculpture, sequence id : 03852')
download_file_from_google_drive('16v6ZZ_DVOfCVDt1_1Qb-lxW09KDnhb-f', dest_dir, '03852.zip')

print('Dowloading dataset : sculpture, sequence id : 03853')
download_file_from_google_drive('1fQqUVckTezxndlf-IxJn1u2A0bX5kSEm', dest_dir, '03853.zip')

print('Dowloading dataset : sculpture, sequence id : 03854')
download_file_from_google_drive('1FiIS_mI_pYWoot3WG-dei2Nke5TNXY-6', dest_dir, '03854.zip')

print('Dowloading dataset : sculpture, sequence id : 03856')
download_file_from_google_drive('1zj1BSHxUKz4piEphXO33lVyTie7T2zdO', dest_dir, '03856.zip')

print('Dowloading dataset : sculpture, sequence id : 03859')
download_file_from_google_drive('100PNCzY3GyaVr-nvQXS4hwth_Fpvm2Zu', dest_dir, '03859.zip')

print('Dowloading dataset : sculpture, sequence id : 03860')
download_file_from_google_drive('17pV5mo_vubUEJSXOC07-n9OCaWS1AOZT', dest_dir, '03860.zip')

print('Dowloading dataset : sculpture, sequence id : 03861')
download_file_from_google_drive('1q7Fx79-1PGHwvE0h_nRaFSWY5jkqVh8i', dest_dir, '03861.zip')

print('Dowloading dataset : sculpture, sequence id : 03870')
download_file_from_google_drive('13aBoK7NvaoK2bYLRqlUKX8bjIJij1z_p', dest_dir, '03870.zip')

print('Dowloading dataset : sculpture, sequence id : 03871')
download_file_from_google_drive('1S8d7Q494BjZg8Uf1YkOurPgfductdgTz', dest_dir, '03871.zip')

print('Dowloading dataset : sculpture, sequence id : 03882')
download_file_from_google_drive('197G6yT2u5Lwiz7TtSev0zzpWV2rhRWR2', dest_dir, '03882.zip')

print('Dowloading dataset : sculpture, sequence id : 03883')
download_file_from_google_drive('1q6jwynbKO2ux_BUzhejfFcIAOGcpQWcf', dest_dir, '03883.zip')

print('Dowloading dataset : sculpture, sequence id : 03884')
download_file_from_google_drive('1O-feXOx-yHiuBKdadW2ViU5zaBxGaGWr', dest_dir, '03884.zip')

print('Dowloading dataset : sculpture, sequence id : 03885')
download_file_from_google_drive('1xZJeyLTRO1HroAHL-T8ChO5o2hfqWc8D', dest_dir, '03885.zip')

print('Dowloading dataset : sculpture, sequence id : 03886')
download_file_from_google_drive('1TCYeqX8N5bbs6zU3PW-MDQpNModzMqZ4', dest_dir, '03886.zip')

print('Dowloading dataset : sculpture, sequence id : 03887')
download_file_from_google_drive('1nVbwKGhxUpP2FkVauFGkjv8_O7pCi2e4', dest_dir, '03887.zip')

print('Dowloading dataset : sculpture, sequence id : 03888')
download_file_from_google_drive('1Qa4pj-xg_KsFvopgCRwaVgjy00CwbP9c', dest_dir, '03888.zip')

print('Dowloading dataset : sculpture, sequence id : 03889')
download_file_from_google_drive('11vGulNvhj-DqF6VUhl9hL8WKqVRAoqao', dest_dir, '03889.zip')

print('Dowloading dataset : sculpture, sequence id : 03890')
download_file_from_google_drive('1iQIQs8ZG_QTvVtEPQv0N9YC3_bUOm3-v', dest_dir, '03890.zip')

print('Dowloading dataset : sculpture, sequence id : 03891')
download_file_from_google_drive('1ntZrQhZGZZla7BPjCKAXvfxVQddHi332', dest_dir, '03891.zip')

print('Dowloading dataset : sculpture, sequence id : 03893')
download_file_from_google_drive('1cbtvKR6O_kV2n9HWxPk0PvktVfwM3OBV', dest_dir, '03893.zip')

print('Dowloading dataset : sculpture, sequence id : 03894')
download_file_from_google_drive('10n51ornqOIDb6J9nb3u9YDA4N50if0BM', dest_dir, '03894.zip')

print('Dowloading dataset : sculpture, sequence id : 03896')
download_file_from_google_drive('11M34xlmtovukrCbXh2_XVVAJc3NpYZG7', dest_dir, '03896.zip')

print('Dowloading dataset : sculpture, sequence id : 03897')
download_file_from_google_drive('11LUXByyq7vYkI4osG8M9C2jymdrtiAwB', dest_dir, '03897.zip')

print('Dowloading dataset : sculpture, sequence id : 03898')
download_file_from_google_drive('1Ei3Qy5ZLOdCtyf2FHqv3OHtKgYZYiq6T', dest_dir, '03898.zip')

print('Dowloading dataset : sculpture, sequence id : 03899')
download_file_from_google_drive('1ix_WekK_GIHAuAPASUiJ45c3Fjhu888n', dest_dir, '03899.zip')

print('Dowloading dataset : sculpture, sequence id : 03900')
download_file_from_google_drive('1B3jxsIjVL7v0VAqOOM3634nayPieCf-0', dest_dir, '03900.zip')

print('Dowloading dataset : sculpture, sequence id : 03901')
download_file_from_google_drive('1wt7QirRD2I2gRJsFTzeyPYe1AKFgoL-T', dest_dir, '03901.zip')

print('Dowloading dataset : sculpture, sequence id : 03916')
download_file_from_google_drive('1ai5uFWlVfueqEpTiHpIqph-dsmlP_A-U', dest_dir, '03916.zip')

print('Dowloading dataset : sculpture, sequence id : 03952')
download_file_from_google_drive('1lk51wnUj6oEaPG7EdPS5-cH9zn3I06Pd', dest_dir, '03952.zip')

print('Dowloading dataset : sculpture, sequence id : 03959')
download_file_from_google_drive('1raZ49wlzfzzke-KIgAYxpcMNYegVUhhn', dest_dir, '03959.zip')

print('Dowloading dataset : sculpture, sequence id : 03960')
download_file_from_google_drive('1f4KGFMdsBgTyEMyWfgnAVuCV-DoGR_Hm', dest_dir, '03960.zip')

print('Dowloading dataset : sculpture, sequence id : 03961')
download_file_from_google_drive('1mHDeidLO-MpihH5RlPMcDT3cDES3FUcn', dest_dir, '03961.zip')

print('Dowloading dataset : sculpture, sequence id : 03962')
download_file_from_google_drive('15W37_3TOI0gHMn_Wmkx_Dr--Gvef8k1s', dest_dir, '03962.zip')

print('Dowloading dataset : sculpture, sequence id : 04112')
download_file_from_google_drive('1qAXXiugi7sXO3CwqHXQ3JSGa5w8zE5Oj', dest_dir, '04112.zip')

print('Dowloading dataset : sculpture, sequence id : 04162')
download_file_from_google_drive('1-FysuBW0kKdqwKLHAGl3M5_zv9FJY8jv', dest_dir, '04162.zip')

print('Dowloading dataset : sculpture, sequence id : 04182')
download_file_from_google_drive('1iWZun7Z7aOqNy_dh7r6UELmXzJKycePa', dest_dir, '04182.zip')

print('Dowloading dataset : sculpture, sequence id : 04219')
download_file_from_google_drive('1c2KkO2okfr6hBzSOFnBWICDa60XEoYTZ', dest_dir, '04219.zip')

print('Dowloading dataset : sculpture, sequence id : 04220')
download_file_from_google_drive('1GUCNV_mFfGai6kw7KGYRuauTxGZ0I_jI', dest_dir, '04220.zip')

print('Dowloading dataset : sculpture, sequence id : 04222')
download_file_from_google_drive('1GXjnLCXTfiySWyqhN9naEBsCdF4NBmfP', dest_dir, '04222.zip')

print('Dowloading dataset : sculpture, sequence id : 04223')
download_file_from_google_drive('1LVDguv_prUeTtiwr9q6y_U2sS8hQlgMd', dest_dir, '04223.zip')

print('Dowloading dataset : sculpture, sequence id : 04224')
download_file_from_google_drive('13fom5GBedWUbCG4xlDNfMcGR9fDmnWse', dest_dir, '04224.zip')

print('Dowloading dataset : sculpture, sequence id : 04225')
download_file_from_google_drive('1mpFkVDAjmREfhLayxcCtdCDqV8qvhras', dest_dir, '04225.zip')

print('Dowloading dataset : sculpture, sequence id : 04226')
download_file_from_google_drive('1FtCyx6RJ9FWXuYcVBktI0zrq-JMZBfgD', dest_dir, '04226.zip')

print('Dowloading dataset : sculpture, sequence id : 04227')
download_file_from_google_drive('1Ze9wf7VzoEUdcUF8HeSZXFA_od1wiBEK', dest_dir, '04227.zip')

print('Dowloading dataset : sculpture, sequence id : 04228')
download_file_from_google_drive('1N9WusB-X3Q_CI1C5rJgEXw-YGTpLMpW6', dest_dir, '04228.zip')

print('Dowloading dataset : sculpture, sequence id : 04229')
download_file_from_google_drive('1Zqk3Dl9xUu8LZYhr37vSJa5sbclBtbSe', dest_dir, '04229.zip')

print('Dowloading dataset : sculpture, sequence id : 04230')
download_file_from_google_drive('14jHyGuMeLaHEeL2lT7s479FwujCbbSK4', dest_dir, '04230.zip')

print('Dowloading dataset : sculpture, sequence id : 04231')
download_file_from_google_drive('1i9et-biTgHEu82ihSMb1IQnMSvSOD4Mr', dest_dir, '04231.zip')

print('Dowloading dataset : sculpture, sequence id : 04232')
download_file_from_google_drive('1CXCRctPpC8SotKQxoZXDlIRGeBfaUn9q', dest_dir, '04232.zip')

print('Dowloading dataset : sculpture, sequence id : 04233')
download_file_from_google_drive('10WcXA1y4PvzJG418rSAyxyBvoOSDt83j', dest_dir, '04233.zip')

print('Dowloading dataset : sculpture, sequence id : 04234')
download_file_from_google_drive('1FNuCrZsUIqku_xHBjVw6ooyyXE3QYZY2', dest_dir, '04234.zip')

print('Dowloading dataset : sculpture, sequence id : 04235')
download_file_from_google_drive('1eJlfhfIov_Wg4XEU087fbhqA9gMvGpTw', dest_dir, '04235.zip')

print('Dowloading dataset : sculpture, sequence id : 04236')
download_file_from_google_drive('17kWVIytMsazLOkw4SJN77bWO92xJJ8aJ', dest_dir, '04236.zip')

print('Dowloading dataset : sculpture, sequence id : 04237')
download_file_from_google_drive('1l9r7tqR-prwWt5AJt6Cb8panVeQzaL2g', dest_dir, '04237.zip')

print('Dowloading dataset : sculpture, sequence id : 04238')
download_file_from_google_drive('18EGK6kEFd3Rq3YGRjf6cuu4GRh2SN10o', dest_dir, '04238.zip')

print('Dowloading dataset : sculpture, sequence id : 04239')
download_file_from_google_drive('1RgiWtdIKTwTPVTzpbBWAmQyXn5cY-EVI', dest_dir, '04239.zip')

print('Dowloading dataset : sculpture, sequence id : 04240')
download_file_from_google_drive('1xOHlvn1qiQ1pKYnlARorzvmZ_edq4Axx', dest_dir, '04240.zip')

print('Dowloading dataset : sculpture, sequence id : 04241')
download_file_from_google_drive('1PvCQlwLzoRilSD8RnlldAK3ukLTKAA4x', dest_dir, '04241.zip')

print('Dowloading dataset : sculpture, sequence id : 04242')
download_file_from_google_drive('1z5MkY3BsMCqAvpZYaVs__bP7rWF5XTD3', dest_dir, '04242.zip')

print('Dowloading dataset : sculpture, sequence id : 04243')
download_file_from_google_drive('1VE7wIySxuL9LukOLKYcbiVyG9X8WnVYq', dest_dir, '04243.zip')

print('Dowloading dataset : sculpture, sequence id : 04244')
download_file_from_google_drive('1-_0-m59dWt80WT6Z3RqOPvMFYK3S2TXg', dest_dir, '04244.zip')

print('Dowloading dataset : sculpture, sequence id : 04245')
download_file_from_google_drive('1WzpLbl8GXGCQ9eJontqtagiP1m7bRbah', dest_dir, '04245.zip')

print('Dowloading dataset : sculpture, sequence id : 04246')
download_file_from_google_drive('1EvR76CIaPpZ9AtrSKDhtfAAW0k6pqOVc', dest_dir, '04246.zip')

print('Dowloading dataset : sculpture, sequence id : 04247')
download_file_from_google_drive('1p--lExzjpb-CKEkqrq5rx0M9jQWk-GYb', dest_dir, '04247.zip')

print('Dowloading dataset : sculpture, sequence id : 04248')
download_file_from_google_drive('1fTPnS9QtAEwN6YmKalIIi7czhAiVIhdw', dest_dir, '04248.zip')

print('Dowloading dataset : sculpture, sequence id : 04249')
download_file_from_google_drive('1_m6Fi0-wPLCHS9DVfXgnui-_mjFcp6Mw', dest_dir, '04249.zip')

print('Dowloading dataset : sculpture, sequence id : 04250')
download_file_from_google_drive('1B7Eo53zGY3JwIRc-WNqeChocDJHzStdA', dest_dir, '04250.zip')

print('Dowloading dataset : sculpture, sequence id : 04251')
download_file_from_google_drive('1guWxjxFtVN-K9LskfKFV3ez-LXoMsYpX', dest_dir, '04251.zip')

print('Dowloading dataset : sculpture, sequence id : 04252')
download_file_from_google_drive('1UtInFlzUwnXHdtS8Kj86uKtBkV3yX52s', dest_dir, '04252.zip')

print('Dowloading dataset : sculpture, sequence id : 04253')
download_file_from_google_drive('1lBTwAiFYc2MZeZVtrgPqhBvEovvI1vsT', dest_dir, '04253.zip')

print('Dowloading dataset : sculpture, sequence id : 04254')
download_file_from_google_drive('1LL6yFuxFGvBZRd2XAdm22z9y6Sxr1ZX0', dest_dir, '04254.zip')

print('Dowloading dataset : sculpture, sequence id : 04255')
download_file_from_google_drive('1ZERm2iJJpStaxkGmTZuz0I2frM1PJrXs', dest_dir, '04255.zip')

print('Dowloading dataset : sculpture, sequence id : 04256')
download_file_from_google_drive('1ObN0H6yInewdBTv26rYzxcoP6F5koiZW', dest_dir, '04256.zip')

print('Dowloading dataset : sculpture, sequence id : 04257')
download_file_from_google_drive('1y35kuiC3WdEt4b02L0B60JL_2mHkrlu_', dest_dir, '04257.zip')

print('Dowloading dataset : sculpture, sequence id : 04258')
download_file_from_google_drive('1dncIQ4aFRIMouicMK4Ldq6CB91npBz2d', dest_dir, '04258.zip')

print('Dowloading dataset : sculpture, sequence id : 04259')
download_file_from_google_drive('1qg8QsucYv09K4a-9b6_ArUoQYXReL6oD', dest_dir, '04259.zip')

print('Dowloading dataset : sculpture, sequence id : 04260')
download_file_from_google_drive('12N2lbCatCO5q8jRgIDXYwqU6UY5EEZrr', dest_dir, '04260.zip')

print('Dowloading dataset : sculpture, sequence id : 04261')
download_file_from_google_drive('1fliUoUnj6U4bxEUkIoMVZ9YwrCwwzPWj', dest_dir, '04261.zip')

print('Dowloading dataset : sculpture, sequence id : 04265')
download_file_from_google_drive('1712MjkIfllbUukTadrFWAM3bvppkL2pd', dest_dir, '04265.zip')

print('Dowloading dataset : sculpture, sequence id : 04266')
download_file_from_google_drive('1E5Mw1_lkoIZHmODgXTha97W0nngtiVW6', dest_dir, '04266.zip')

print('Dowloading dataset : sculpture, sequence id : 04267')
download_file_from_google_drive('1xSu4qAZsuD-UTHTc-WdJL5zP71Mu32fD', dest_dir, '04267.zip')

print('Dowloading dataset : sculpture, sequence id : 04268')
download_file_from_google_drive('10HmsZJw5uPwT4udFCFBPGYlKZ1yV-S8S', dest_dir, '04268.zip')

print('Dowloading dataset : sculpture, sequence id : 04269')
download_file_from_google_drive('1H73h8T0RjEB4Xeh7jc_Yhe562rLIsA08', dest_dir, '04269.zip')

print('Dowloading dataset : sculpture, sequence id : 04270')
download_file_from_google_drive('11jR0zAqFUJys7NeuPPN8WAednvaffiCS', dest_dir, '04270.zip')

print('Dowloading dataset : sculpture, sequence id : 04271')
download_file_from_google_drive('12D_J210Jwxfbtavn1MxTUTDibv9DyztL', dest_dir, '04271.zip')

print('Dowloading dataset : sculpture, sequence id : 04272')
download_file_from_google_drive('1S15K5pJH_Cn4zUrVZIyotqD0ctCWptK4', dest_dir, '04272.zip')

print('Dowloading dataset : sculpture, sequence id : 04273')
download_file_from_google_drive('1nsIUkwEuvkLcns8iuYzevQJ2u3vhzxFF', dest_dir, '04273.zip')

print('Dowloading dataset : sculpture, sequence id : 04274')
download_file_from_google_drive('1zbXXWLsjEhr7ZOC1xZaJU28nW3GChABH', dest_dir, '04274.zip')

print('Dowloading dataset : sculpture, sequence id : 04275')
download_file_from_google_drive('1UksjXquPHhU75g3wcqsLNEQgQNhg0AdW', dest_dir, '04275.zip')

print('Dowloading dataset : sculpture, sequence id : 04276')
download_file_from_google_drive('1KjWNkp--NVaQiJR82KAh1JjH6xyB60x0', dest_dir, '04276.zip')

print('Dowloading dataset : sculpture, sequence id : 04277')
download_file_from_google_drive('11WljEsGM9Oabn4YWitvlCrNKWoHzF5oU', dest_dir, '04277.zip')

print('Dowloading dataset : sculpture, sequence id : 04278')
download_file_from_google_drive('1KYITF_z1lOSkYMrEu6LT4kxefRYJ3Hdh', dest_dir, '04278.zip')

print('Dowloading dataset : sculpture, sequence id : 04279')
download_file_from_google_drive('1lMOsaOVMmBzwK07ECVBZvkSqp3rQIurd', dest_dir, '04279.zip')

print('Dowloading dataset : sculpture, sequence id : 04280')
download_file_from_google_drive('1LL1H-ZPHHzaNDHnInpc8UIAbMbbly-Ur', dest_dir, '04280.zip')

print('Dowloading dataset : sculpture, sequence id : 04281')
download_file_from_google_drive('10oA5uEoqBjLNum724hXnoQKUjOs5ADAI', dest_dir, '04281.zip')

print('Dowloading dataset : sculpture, sequence id : 04282')
download_file_from_google_drive('10yIn6XwfKfmPMv2Qs3SOBISQ7sMt9_Wk', dest_dir, '04282.zip')

print('Dowloading dataset : sculpture, sequence id : 04283')
download_file_from_google_drive('1ipNYZ617O8fr859Dx7kIE7hEdaK4Mtpt', dest_dir, '04283.zip')

print('Dowloading dataset : sculpture, sequence id : 04284')
download_file_from_google_drive('1fHjm0cLmipQSMjAGJNIy2iohJnUQ51BK', dest_dir, '04284.zip')

print('Dowloading dataset : sculpture, sequence id : 04285')
download_file_from_google_drive('15W4N9-yoAjRjkXN64fEBWWqxU0TAYmwA', dest_dir, '04285.zip')

print('Dowloading dataset : sculpture, sequence id : 04286')
download_file_from_google_drive('1JkYThNiwPXGeyL2mAYlaUVjVHOUS5q1W', dest_dir, '04286.zip')

print('Dowloading dataset : sculpture, sequence id : 04287')
download_file_from_google_drive('1NI47_k7ZVKdvYjqVgWbPmmszFuMyZ0Sy', dest_dir, '04287.zip')

print('Dowloading dataset : sculpture, sequence id : 04288')
download_file_from_google_drive('1KdqCwZ8DALBIGjIyKhFXxC-vsX4RH08f', dest_dir, '04288.zip')

print('Dowloading dataset : sculpture, sequence id : 04289')
download_file_from_google_drive('1TR32CumSv_9c1bxUuXBVnlahMlVFJ0zp', dest_dir, '04289.zip')

print('Dowloading dataset : sculpture, sequence id : 04290')
download_file_from_google_drive('1I_k3j-SbJFqSzenId7ca_wKBSKQC81em', dest_dir, '04290.zip')

print('Dowloading dataset : sculpture, sequence id : 04291')
download_file_from_google_drive('1KIk3L9sdmwoZ8RFFQ5RHaNKrIUH4y6TY', dest_dir, '04291.zip')

print('Dowloading dataset : sculpture, sequence id : 04292')
download_file_from_google_drive('1SAC8kVo45dla9q-Ikv9EpoO6Xe_4ao_U', dest_dir, '04292.zip')

print('Dowloading dataset : sculpture, sequence id : 04293')
download_file_from_google_drive('1VnJqhtoRj9569twoqHA8WDZP9oUZXGau', dest_dir, '04293.zip')

print('Dowloading dataset : sculpture, sequence id : 04294')
download_file_from_google_drive('16dqQpH3nBhA8gPLs4FrK91DQ_lv8H5kD', dest_dir, '04294.zip')

print('Dowloading dataset : sculpture, sequence id : 04493')
download_file_from_google_drive('16HbXYLBv8S4e7EAFRF72It58tibRPSpd', dest_dir, '04493.zip')

print('Dowloading dataset : sculpture, sequence id : 04524')
download_file_from_google_drive('1QqiTH_N2vEk8aL7gTHLojiUsWkJw-fvC', dest_dir, '04524.zip')

print('Dowloading dataset : sculpture, sequence id : 04535')
download_file_from_google_drive('1ibsUp-GSmIOWrAodAyxlkVUan3av-Oy1', dest_dir, '04535.zip')

print('Dowloading dataset : sculpture, sequence id : 04536')
download_file_from_google_drive('1ye-4b_ggM-tEafYax1_Id_JCO_jS8NTa', dest_dir, '04536.zip')

print('Dowloading dataset : sculpture, sequence id : 04541')
download_file_from_google_drive('1AJmQKcBFixWVShcEwtDLbCfLZIJ4grjq', dest_dir, '04541.zip')

print('Dowloading dataset : sculpture, sequence id : 04566')
download_file_from_google_drive('1hqA_mYH_VzsQxtV2LrMeLMylTrZJwlNT', dest_dir, '04566.zip')

print('Dowloading dataset : sculpture, sequence id : 04567')
download_file_from_google_drive('1Q0i-sQWT-qlc18BHLPReiIeH6T_61M_I', dest_dir, '04567.zip')

print('Dowloading dataset : sculpture, sequence id : 04569')
download_file_from_google_drive('1PRaVADDGtyUi3WBcdIMq0_xey84wVrzW', dest_dir, '04569.zip')

print('Dowloading dataset : sculpture, sequence id : 04570')
download_file_from_google_drive('1ooEBaLpb_wNJ0Ap3hgCRHX09JA1PEs-j', dest_dir, '04570.zip')

print('Dowloading dataset : sculpture, sequence id : 04571')
download_file_from_google_drive('1ePDvIhQss5roma5GR3ZparfESVwQeOxn', dest_dir, '04571.zip')

print('Dowloading dataset : sculpture, sequence id : 05022')
download_file_from_google_drive('1gUPkiJ7_Hr75FZH4AvyAAn1Oogwlg-ge', dest_dir, '05022.zip')

print('Dowloading dataset : sculpture, sequence id : 05025')
download_file_from_google_drive('1ulRMwwuEQJVNbCuTBajEDrZ3KkTNfiut', dest_dir, '05025.zip')

print('Dowloading dataset : sculpture, sequence id : 05055')
download_file_from_google_drive('1gQUZkxL40Yvk9DZAs1adEI7B2jZGsJ1M', dest_dir, '05055.zip')

print('Dowloading dataset : sculpture, sequence id : 05121')
download_file_from_google_drive('1ZKeVyMdstqgxzp62DqC7Yx63IiFmQsG4', dest_dir, '05121.zip')

print('Dowloading dataset : sculpture, sequence id : 05122')
download_file_from_google_drive('1_zDNLYMMAvCBlSq6zrfUci9c22iA3GE3', dest_dir, '05122.zip')

print('Dowloading dataset : sculpture, sequence id : 05124')
download_file_from_google_drive('1cObDtNkBq0C5fCGRIc67I8DLL4yWzLkL', dest_dir, '05124.zip')

print('Dowloading dataset : sculpture, sequence id : 05125')
download_file_from_google_drive('1_KOcI03MwItcnGoQjchFTE7Uega40NNf', dest_dir, '05125.zip')

print('Dowloading dataset : sculpture, sequence id : 05126')
download_file_from_google_drive('1uCTPneuZGAkGeqi9zv3Egy4J4iTUHPIq', dest_dir, '05126.zip')

print('Dowloading dataset : sculpture, sequence id : 05127')
download_file_from_google_drive('1AyLVz4UsBYwr_xIP53624MxrOWVXm3wF', dest_dir, '05127.zip')

print('Dowloading dataset : sculpture, sequence id : 05128')
download_file_from_google_drive('1aG2JbsNgNE9tcY1jDrZL9NxMGm-yEIeF', dest_dir, '05128.zip')

print('Dowloading dataset : sculpture, sequence id : 05129')
download_file_from_google_drive('1418NbW9_wn8zMeaDua4Ae8QyZj16mjh3', dest_dir, '05129.zip')

print('Dowloading dataset : sculpture, sequence id : 05130')
download_file_from_google_drive('1su0Nbg1jy8BjjfyL-rhJf691v313xy_W', dest_dir, '05130.zip')

print('Dowloading dataset : sculpture, sequence id : 05131')
download_file_from_google_drive('1VYhbbqjoi66SGRM5ukIitP-6XRdOTeoj', dest_dir, '05131.zip')

print('Dowloading dataset : sculpture, sequence id : 05132')
download_file_from_google_drive('1lJkteFZtYrYjNLvPnCK8GTb_U9furVnE', dest_dir, '05132.zip')

print('Dowloading dataset : sculpture, sequence id : 05133')
download_file_from_google_drive('12-IxmibJXcEyqvTBYTa635gr83hqgLav', dest_dir, '05133.zip')

print('Dowloading dataset : sculpture, sequence id : 05134')
download_file_from_google_drive('1dAzuemwNFMhdZsy4Sjox88YRMGeaHWSm', dest_dir, '05134.zip')

print('Dowloading dataset : sculpture, sequence id : 05135')
download_file_from_google_drive('1Oykk-SjUK7VVAD6AoCyI2Ge5PbfX1UrF', dest_dir, '05135.zip')

print('Dowloading dataset : sculpture, sequence id : 05136')
download_file_from_google_drive('1346aYeY_kpW4KPQORORRa_oYbAq7b2sE', dest_dir, '05136.zip')

print('Dowloading dataset : sculpture, sequence id : 05137')
download_file_from_google_drive('1Yn1JrDkTgkW16dDGfJhVPApkvxFJOQ0P', dest_dir, '05137.zip')

print('Dowloading dataset : sculpture, sequence id : 05138')
download_file_from_google_drive('1YQDVIyUBKAr-xibcl9cZYBQrS-bz-5gR', dest_dir, '05138.zip')

print('Dowloading dataset : sculpture, sequence id : 05139')
download_file_from_google_drive('1nJ2WLY6h6PmVn3Gqr68D2g9PfAEQ3h1a', dest_dir, '05139.zip')

print('Dowloading dataset : sculpture, sequence id : 05140')
download_file_from_google_drive('1iGMBNMzS1pp4DqwFfqnuGz7WL20BhgGZ', dest_dir, '05140.zip')

print('Dowloading dataset : sculpture, sequence id : 05141')
download_file_from_google_drive('1wXwOl8Cpaqn7Q76LnL7ytrUgXTKwJR-J', dest_dir, '05141.zip')

print('Dowloading dataset : sculpture, sequence id : 05142')
download_file_from_google_drive('1qPoFqBcpmYYRBQtpvW3XaUc2gEC0igbZ', dest_dir, '05142.zip')

print('Dowloading dataset : sculpture, sequence id : 05143')
download_file_from_google_drive('1P25pnPJVfN23El5k530nXcVy9aY4U4dV', dest_dir, '05143.zip')

print('Dowloading dataset : sculpture, sequence id : 05144')
download_file_from_google_drive('1bo7PPt-OxJTa03VRtLb8ENF5AIKQ2Fif', dest_dir, '05144.zip')

print('Dowloading dataset : sculpture, sequence id : 05145')
download_file_from_google_drive('1YiDL8B5z1jCxnfGnYUCxDG_Z8f9g5qM8', dest_dir, '05145.zip')

print('Dowloading dataset : sculpture, sequence id : 05146')
download_file_from_google_drive('160eoJmqt4QidEHrpFCzRjzHkU-NdqB6S', dest_dir, '05146.zip')

print('Dowloading dataset : sculpture, sequence id : 05148')
download_file_from_google_drive('1hDSM6ToN0jZ6XBim7J0pgnxJ7tC6Ouh7', dest_dir, '05148.zip')

print('Dowloading dataset : sculpture, sequence id : 05149')
download_file_from_google_drive('1-deFHfWHglsQzOgpA612kpDZO0uAfENW', dest_dir, '05149.zip')

print('Dowloading dataset : sculpture, sequence id : 05151')
download_file_from_google_drive('1Qpm8p2WzP2Rx4kD5oHi4FKRsCbP3Fbp3', dest_dir, '05151.zip')

print('Dowloading dataset : sculpture, sequence id : 05152')
download_file_from_google_drive('16fgGHrBAzG9davPyWFC2gKL_yyOmYi_I', dest_dir, '05152.zip')

print('Dowloading dataset : sculpture, sequence id : 05154')
download_file_from_google_drive('1MI0yMOTVmd6V5N_2CXoNzPgdXNKAh_3l', dest_dir, '05154.zip')

print('Dowloading dataset : sculpture, sequence id : 05155')
download_file_from_google_drive('1MY8miUuEOq4VvL7IlGk40uEs7_lawDya', dest_dir, '05155.zip')

print('Dowloading dataset : sculpture, sequence id : 05156')
download_file_from_google_drive('1X_NISmFtG9FYgAbIOTtAPlBcDm61Gik7', dest_dir, '05156.zip')

print('Dowloading dataset : sculpture, sequence id : 05157')
download_file_from_google_drive('1LkR9osc5QDnbEgNB41QEjzu8R1DVHjdE', dest_dir, '05157.zip')

print('Dowloading dataset : sculpture, sequence id : 05158')
download_file_from_google_drive('1pgRa9oNoQrWCfQbGWkF5xNlabcfg1huC', dest_dir, '05158.zip')

print('Dowloading dataset : sculpture, sequence id : 05159')
download_file_from_google_drive('1lWuDEhYe7YDkeUAbhV2szHwS8lYxed5e', dest_dir, '05159.zip')

print('Dowloading dataset : sculpture, sequence id : 05160')
download_file_from_google_drive('141EjvPgx0KCWDn7CchPSuJp2e2qRJyuI', dest_dir, '05160.zip')

print('Dowloading dataset : sculpture, sequence id : 05161')
download_file_from_google_drive('15yl_j0XY9NFmZy3o8VH738RHewyxvdus', dest_dir, '05161.zip')

print('Dowloading dataset : sculpture, sequence id : 05162')
download_file_from_google_drive('1e2HXHaAh8gUsYpi__22p_0EtTsXd9QzR', dest_dir, '05162.zip')

print('Dowloading dataset : sculpture, sequence id : 05163')
download_file_from_google_drive('1PT8b1cPXkSYaKM31bxHZAJJfZIOVhRfQ', dest_dir, '05163.zip')

print('Dowloading dataset : sculpture, sequence id : 05164')
download_file_from_google_drive('1C90ESavCEShh1DBoHSJGGqsvKH07C4Ps', dest_dir, '05164.zip')

print('Dowloading dataset : sculpture, sequence id : 05165')
download_file_from_google_drive('1jCzC6MBUn84OkI8lsegHsamC7-3zBZrq', dest_dir, '05165.zip')

print('Dowloading dataset : sculpture, sequence id : 05166')
download_file_from_google_drive('117yzgmDWgn3MitKUfzHLKKZjtbbuz-iy', dest_dir, '05166.zip')

print('Dowloading dataset : sculpture, sequence id : 05167')
download_file_from_google_drive('1PCSszTtfDF2pK4RUUw3EnDEltw0cZFx_', dest_dir, '05167.zip')

print('Dowloading dataset : sculpture, sequence id : 05168')
download_file_from_google_drive('1I3TPZjcRq1EVURSUJkrNyqA7AJpIQfrg', dest_dir, '05168.zip')

print('Dowloading dataset : sculpture, sequence id : 05169')
download_file_from_google_drive('1DQL0A20urb3tyYHEzFgMX7PgyhojLiSq', dest_dir, '05169.zip')

print('Dowloading dataset : sculpture, sequence id : 05170')
download_file_from_google_drive('188WierJHuBjtBaG3xGnO1-QbK8OB4TVo', dest_dir, '05170.zip')

print('Dowloading dataset : sculpture, sequence id : 05171')
download_file_from_google_drive('1buAW8O9uD_H9Cy6_EhwHiZ99LlksKtzJ', dest_dir, '05171.zip')

print('Dowloading dataset : sculpture, sequence id : 05172')
download_file_from_google_drive('1wot1dIj4gHrzlZKrOT1VaBtisb41Mjrs', dest_dir, '05172.zip')

print('Dowloading dataset : sculpture, sequence id : 05173')
download_file_from_google_drive('1csimZjMJLuptMXv9k0BIIHwYtcaVlxWD', dest_dir, '05173.zip')

print('Dowloading dataset : sculpture, sequence id : 05174')
download_file_from_google_drive('1yIJIJwM9BAFmya9jZqgE328aSHLHC8Ef', dest_dir, '05174.zip')

print('Dowloading dataset : sculpture, sequence id : 05175')
download_file_from_google_drive('1rFMn7CxMLACEdEy1mKWbU-VmXHBUXlEx', dest_dir, '05175.zip')

print('Dowloading dataset : sculpture, sequence id : 05176')
download_file_from_google_drive('1QxQsGDDNItVHLNrPJIzPhxc9m3xHGgX6', dest_dir, '05176.zip')

print('Dowloading dataset : sculpture, sequence id : 05177')
download_file_from_google_drive('1r88S46R-0WhJRhme-N8901Ub1HN0iILl', dest_dir, '05177.zip')

print('Dowloading dataset : sculpture, sequence id : 05178')
download_file_from_google_drive('1h7D7Q99i_KxLa9rjkHPBtbdWD63VH-jj', dest_dir, '05178.zip')

print('Dowloading dataset : sculpture, sequence id : 05193')
download_file_from_google_drive('1yO-09mP7VxjWTsSAS2Rrjy51h6bT3ilV', dest_dir, '05193.zip')

print('Dowloading dataset : sculpture, sequence id : 05197')
download_file_from_google_drive('1LtKQo_RRKRkJlSeJDLsK-GnP815Bz_yv', dest_dir, '05197.zip')

print('Dowloading dataset : sculpture, sequence id : 05198')
download_file_from_google_drive('1S2SCqlVUMsrnuT-wAKC5O9QIRIvUY1BM', dest_dir, '05198.zip')

print('Dowloading dataset : sculpture, sequence id : 05199')
download_file_from_google_drive('1PRFRIsvJiDt3JmjA6lN98T2hYMvV2KoW', dest_dir, '05199.zip')

print('Dowloading dataset : sculpture, sequence id : 05200')
download_file_from_google_drive('1eygDVBLb6Tw1J8fQcTeiGtARjhJjGG3B', dest_dir, '05200.zip')

print('Dowloading dataset : sculpture, sequence id : 05201')
download_file_from_google_drive('1Syoj2zSjrbzuqm55IeczE3j3pIaef8MW', dest_dir, '05201.zip')

print('Dowloading dataset : sculpture, sequence id : 05202')
download_file_from_google_drive('1FELoUiLPxratf6q-ZDh-vrCU7at9szWy', dest_dir, '05202.zip')

print('Dowloading dataset : sculpture, sequence id : 05203')
download_file_from_google_drive('1F-cmmD-q8YPT__xp2_zj69rJjllBGUey', dest_dir, '05203.zip')

print('Dowloading dataset : sculpture, sequence id : 05204')
download_file_from_google_drive('1xMxX-pfCGWXZYs1VU_4yFJPg-lvDnhNe', dest_dir, '05204.zip')

print('Dowloading dataset : sculpture, sequence id : 05205')
download_file_from_google_drive('1AlKiQPRQ1JOU97SaxBFccQF7_Gla97Sj', dest_dir, '05205.zip')

print('Dowloading dataset : sculpture, sequence id : 05206')
download_file_from_google_drive('1GEIcFieUU4fzPlEBlRfNwKG7xMVovpgy', dest_dir, '05206.zip')

print('Dowloading dataset : sculpture, sequence id : 05207')
download_file_from_google_drive('1KPH8Iy3-iOXiuGEQo6UkFrANtxZXVq__', dest_dir, '05207.zip')

print('Dowloading dataset : sculpture, sequence id : 05212')
download_file_from_google_drive('1B95cytRGe7cHzE4fIcmCfZfnoTjgw5fl', dest_dir, '05212.zip')

print('Dowloading dataset : sculpture, sequence id : 05213')
download_file_from_google_drive('1JOxLdpqht8B4QB6-SO02buXPZ3IDtrKS', dest_dir, '05213.zip')

print('Dowloading dataset : sculpture, sequence id : 05216')
download_file_from_google_drive('1Y2hiKRyaymhyI2if1rH8k3yPt2eO002o', dest_dir, '05216.zip')

print('Dowloading dataset : sculpture, sequence id : 05222')
download_file_from_google_drive('1qwpcxxvcffJDzlkhihiQYwsLaG2ZLAI8', dest_dir, '05222.zip')

print('Dowloading dataset : sculpture, sequence id : 05223')
download_file_from_google_drive('1JJbQWcKNmCHbgY5ftSlmQvS005rgFpxt', dest_dir, '05223.zip')

print('Dowloading dataset : sculpture, sequence id : 05224')
download_file_from_google_drive('1LO6wFftlf-xv9DFoG6-hG6sqP_--0LiL', dest_dir, '05224.zip')

print('Dowloading dataset : sculpture, sequence id : 05225')
download_file_from_google_drive('1boEkaTiq9OE8sJKrfK-mp2ymXHerqoOr', dest_dir, '05225.zip')

print('Dowloading dataset : sculpture, sequence id : 05226')
download_file_from_google_drive('1usqfE2LXQdD2qYbFCoBzOnTpIDkLtSf8', dest_dir, '05226.zip')

print('Dowloading dataset : sculpture, sequence id : 05227')
download_file_from_google_drive('1qS-iLpmrc2fN0W0wh3RYFyaavD_8yxcS', dest_dir, '05227.zip')

print('Dowloading dataset : sculpture, sequence id : 05228')
download_file_from_google_drive('1fbQ-hxQiSdhHJmMtiVeIBckp5teYzmDa', dest_dir, '05228.zip')

print('Dowloading dataset : sculpture, sequence id : 05229')
download_file_from_google_drive('1AbcU2WbWQ-QeAtOcGl5qYNZyXt1F94CK', dest_dir, '05229.zip')

print('Dowloading dataset : sculpture, sequence id : 05230')
download_file_from_google_drive('1ud4UOrA3cIeRRqFxEmrSbpimgv3gZIev', dest_dir, '05230.zip')

print('Dowloading dataset : sculpture, sequence id : 05232')
download_file_from_google_drive('1TK5NUH4PUliuNYNuGwuTzVv-9Y_AjkTH', dest_dir, '05232.zip')

print('Dowloading dataset : sculpture, sequence id : 05233')
download_file_from_google_drive('1LpReHAtkVd4tQZDl_AsOt7cFu28wHeD3', dest_dir, '05233.zip')

print('Dowloading dataset : sculpture, sequence id : 05234')
download_file_from_google_drive('13Nr5z6JrMH8oqQOeypEjzpGR2WLUFZpC', dest_dir, '05234.zip')

print('Dowloading dataset : sculpture, sequence id : 05235')
download_file_from_google_drive('1zKFvDDqHcj53t0NMw9bHaOpusH54QBYC', dest_dir, '05235.zip')

print('Dowloading dataset : sculpture, sequence id : 05236')
download_file_from_google_drive('1gn_x4cOs3joTNyKYGOXRyImWZ_Zj0yP3', dest_dir, '05236.zip')

print('Dowloading dataset : sculpture, sequence id : 05237')
download_file_from_google_drive('1S0mHel_MUGm-6mtDZLNvrkXF8UrJtyN-', dest_dir, '05237.zip')

print('Dowloading dataset : sculpture, sequence id : 05238')
download_file_from_google_drive('1BKcV-Y6S7FTNJrw0Rt639sWRgZFNzlfi', dest_dir, '05238.zip')

print('Dowloading dataset : sculpture, sequence id : 05244')
download_file_from_google_drive('1oxCRFgRw5pcSFpzlLcMw6qYj6DVPloUY', dest_dir, '05244.zip')

print('Dowloading dataset : sculpture, sequence id : 05247')
download_file_from_google_drive('1su3-IbDcP66Dd2wogLdL7dX2Tw71jOy1', dest_dir, '05247.zip')

print('Dowloading dataset : sculpture, sequence id : 05248')
download_file_from_google_drive('1Iy7t97V2X7l67GOeRZTC4-LQSKCHHT4w', dest_dir, '05248.zip')

print('Dowloading dataset : sculpture, sequence id : 05249')
download_file_from_google_drive('1J7EA9sCR33Udh6h0wxHUTl8kpR01Q3du', dest_dir, '05249.zip')

print('Dowloading dataset : sculpture, sequence id : 05250')
download_file_from_google_drive('15N_vuGzff65fxSqaaMrb1_hdj3ebziZM', dest_dir, '05250.zip')

print('Dowloading dataset : sculpture, sequence id : 05536')
download_file_from_google_drive('1No2XzuLmEaQeJv6ECZ2yYAYdA9gJx79q', dest_dir, '05536.zip')

print('Dowloading dataset : sculpture, sequence id : 05539')
download_file_from_google_drive('1Pw5OczS_SwKStwOPpIg8qtiUBIfe8FOL', dest_dir, '05539.zip')

print('Dowloading dataset : sculpture, sequence id : 05627')
download_file_from_google_drive('1h79EBiiQinYyv8XzkdMVWh_Me7JR_8AN', dest_dir, '05627.zip')

print('Dowloading dataset : sculpture, sequence id : 05738')
download_file_from_google_drive('1Ri_9-Qu8JyPLnk8_k9XadpLApfsvSfE_', dest_dir, '05738.zip')

print('Dowloading dataset : sculpture, sequence id : 05739')
download_file_from_google_drive('1b6krrrJZgm25G8FdoTJpVtFDSRRZ_BC0', dest_dir, '05739.zip')

print('Dowloading dataset : sculpture, sequence id : 05740')
download_file_from_google_drive('10pdPaWboZDDyfmbKwPkPGL5n11M4qYY7', dest_dir, '05740.zip')

print('Dowloading dataset : sculpture, sequence id : 05741')
download_file_from_google_drive('1yV24KcZqN6MJu07rY2wKK61JS7igaI79', dest_dir, '05741.zip')

print('Dowloading dataset : sculpture, sequence id : 05742')
download_file_from_google_drive('10pv1xy81KWrqa8-eEnldcKky2K1Ov-0d', dest_dir, '05742.zip')

print('Dowloading dataset : sculpture, sequence id : 05743')
download_file_from_google_drive('1t4kJvgzBYPhiqALjZHsWgP3Lr4iyECJA', dest_dir, '05743.zip')

print('Dowloading dataset : sculpture, sequence id : 05744')
download_file_from_google_drive('16JckDWkYGkblJZxoxv2aY4OG7c40Wswn', dest_dir, '05744.zip')

print('Dowloading dataset : sculpture, sequence id : 05745')
download_file_from_google_drive('1b_2XoloENdNx7ukyHNTO4n3YtBYOS9lf', dest_dir, '05745.zip')

print('Dowloading dataset : sculpture, sequence id : 05746')
download_file_from_google_drive('1BQivfuZ6HdZcTzvgatdkDYOVDuVgqTlE', dest_dir, '05746.zip')

print('Dowloading dataset : sculpture, sequence id : 05747')
download_file_from_google_drive('1zr0ymfPzWSd6uc3SSknGqdh73LlY8W-c', dest_dir, '05747.zip')

print('Dowloading dataset : sculpture, sequence id : 05748')
download_file_from_google_drive('1tr6ABi5vqEPlz2T5RLYsxcFd299YCybN', dest_dir, '05748.zip')

print('Dowloading dataset : sculpture, sequence id : 05749')
download_file_from_google_drive('11pjRggu8HYUlUtcBymA_LbDenTVyy_Rn', dest_dir, '05749.zip')

print('Dowloading dataset : sculpture, sequence id : 05833')
download_file_from_google_drive('1R9jVk4Quoy-GVF5C-8wkZ5yaueRrQpoe', dest_dir, '05833.zip')

print('Dowloading dataset : sculpture, sequence id : 05834')
download_file_from_google_drive('1Zr4O2P3lcN-8e63o20k3_MCdUXTrktdG', dest_dir, '05834.zip')

print('Dowloading dataset : sculpture, sequence id : 05837')
download_file_from_google_drive('1ozRxbdcMz4q8ba2ORgPoLutv44tjwPny', dest_dir, '05837.zip')

print('Dowloading dataset : sculpture, sequence id : 05839')
download_file_from_google_drive('1eWNOaSqFpNTJOrs-PXBPqZRcQVqHQGG6', dest_dir, '05839.zip')

print('Dowloading dataset : sculpture, sequence id : 05840')
download_file_from_google_drive('1R2_eCpGGwtDPCmpL75Phvwnhc8d39hkY', dest_dir, '05840.zip')

print('Dowloading dataset : sculpture, sequence id : 05920')
download_file_from_google_drive('1DxDdbgJCn_bPm98XwKDTrl2ikvZAEpdG', dest_dir, '05920.zip')

print('Dowloading dataset : sculpture, sequence id : 05921')
download_file_from_google_drive('1Xtpc4L1AmOSDMg40F2_qayonFtd-b-m6', dest_dir, '05921.zip')

print('Dowloading dataset : sculpture, sequence id : 05994')
download_file_from_google_drive('1FVNB_xvWc0hOT_Ol3SWpmIBfJSrwlT2n', dest_dir, '05994.zip')

print('Dowloading dataset : sculpture, sequence id : 06076')
download_file_from_google_drive('1DaZ41Jz6YQCThzqxNTFrPVnes0YbvB8Z', dest_dir, '06076.zip')

print('Dowloading dataset : sculpture, sequence id : 06132')
download_file_from_google_drive('1EZEH75EMq4CaKWDFsjNI9bnSeMeLCUCY', dest_dir, '06132.zip')

print('Dowloading dataset : sculpture, sequence id : 06143')
download_file_from_google_drive('1BXjTP5TA1L_SIGnHjGZAQYcGSS0sniQH', dest_dir, '06143.zip')

print('Dowloading dataset : sculpture, sequence id : 06195')
download_file_from_google_drive('1UZr7Rtrd6Gi_2zXDkZef4VKXHZUOZcBt', dest_dir, '06195.zip')

print('Dowloading dataset : sculpture, sequence id : 06196')
download_file_from_google_drive('1zQRH1OADQiq5t8rhL_uCB6awVXGc1sw9', dest_dir, '06196.zip')

print('Dowloading dataset : sculpture, sequence id : 06197')
download_file_from_google_drive('1tzrjtxb_vyEW6HvjQ0HeIsuW0LkWY1vL', dest_dir, '06197.zip')

print('Dowloading dataset : sculpture, sequence id : 06199')
download_file_from_google_drive('1wwKqx8wLPUeTlq8r62mw9p0tPw_ZFVED', dest_dir, '06199.zip')

print('Dowloading dataset : sculpture, sequence id : 06202')
download_file_from_google_drive('1GNzGPIyJVmcRGgGjWB9wRblPUbsVLA61', dest_dir, '06202.zip')

print('Dowloading dataset : sculpture, sequence id : 06203')
download_file_from_google_drive('1E8XkiIZeebEgYCkIw6LVt2s8zrxoZAmg', dest_dir, '06203.zip')

print('Dowloading dataset : sculpture, sequence id : 06204')
download_file_from_google_drive('1x-yGbUfIP_voqrdW_g64hazAmPN2J1AH', dest_dir, '06204.zip')

print('Dowloading dataset : sculpture, sequence id : 06206')
download_file_from_google_drive('1cfta-25sFyV5M0gX36dY4gnIydP-0hpL', dest_dir, '06206.zip')

print('Dowloading dataset : sculpture, sequence id : 06224')
download_file_from_google_drive('1vBBkzYncAlk8nrpsJJmgRGoiNgGqvFHN', dest_dir, '06224.zip')

print('Dowloading dataset : sculpture, sequence id : 06287')
download_file_from_google_drive('1JTTPS_zU7cbwJzcp9q58NdAiq2E7E0_z', dest_dir, '06287.zip')

print('Dowloading dataset : sculpture, sequence id : 06339')
download_file_from_google_drive('1ZEzHyg6iOISAd_sNlkjCssQJKOeeketS', dest_dir, '06339.zip')

print('Dowloading dataset : sculpture, sequence id : 06350')
download_file_from_google_drive('1YFGer9hqTCo56139j3nJuLCWfIOJW75-', dest_dir, '06350.zip')

print('Dowloading dataset : sculpture, sequence id : 06351')
download_file_from_google_drive('16XTmagJc9Ea8ybZuatNu-dTKkzFZArRK', dest_dir, '06351.zip')

print('Dowloading dataset : sculpture, sequence id : 06352')
download_file_from_google_drive('1b8JdtAzmPetb80gtWuW6Jh2vOkhwyGAO', dest_dir, '06352.zip')

print('Dowloading dataset : sculpture, sequence id : 06353')
download_file_from_google_drive('1GZ1TaMNY45w2bw-e1Y220l8U9I0FMkTD', dest_dir, '06353.zip')

print('Dowloading dataset : sculpture, sequence id : 06363')
download_file_from_google_drive('16LtWoYubfmmT9lZ3HTnCX6exfefroq00', dest_dir, '06363.zip')

print('Dowloading dataset : sculpture, sequence id : 06364')
download_file_from_google_drive('1RQBa5r8yHpO-Yb0DIHAn5qKinOqGhYuM', dest_dir, '06364.zip')

print('Dowloading dataset : sculpture, sequence id : 06367')
download_file_from_google_drive('1m_pwNld_ixyMsvCB1I8PIDn2jyU2z8tw', dest_dir, '06367.zip')

print('Dowloading dataset : sculpture, sequence id : 06368')
download_file_from_google_drive('1FjMwV0FVZL5K1t1xXkrslgxxFgps8sRT', dest_dir, '06368.zip')

print('Dowloading dataset : sculpture, sequence id : 06369')
download_file_from_google_drive('1-TBmEiVXk0GKwsrbzgSspgDgVm7sX6Bz', dest_dir, '06369.zip')

print('Dowloading dataset : sculpture, sequence id : 06370')
download_file_from_google_drive('1wWJ97ZWHgCWDWgJ4aIwK0KxnlbWCFMps', dest_dir, '06370.zip')

print('Dowloading dataset : sculpture, sequence id : 06371')
download_file_from_google_drive('1egk4UzQs4qhrP2q657WxI5CgRAqPnbIh', dest_dir, '06371.zip')

print('Dowloading dataset : sculpture, sequence id : 06372')
download_file_from_google_drive('1i7PgWJOIgRIoe7f0vSVZJNwLk-shNDZE', dest_dir, '06372.zip')

print('Dowloading dataset : sculpture, sequence id : 06373')
download_file_from_google_drive('1YDgDiCmMW5YhprlNQht9BCZEcpuN4pzH', dest_dir, '06373.zip')

print('Dowloading dataset : sculpture, sequence id : 06374')
download_file_from_google_drive('1H1AnzKWlSqoP6zmhqHUjI1g__3v4Ey6k', dest_dir, '06374.zip')

print('Dowloading dataset : sculpture, sequence id : 06375')
download_file_from_google_drive('188hf66MLlZzBStf8LYNPTx04Q3eyGPLN', dest_dir, '06375.zip')

print('Dowloading dataset : sculpture, sequence id : 06376')
download_file_from_google_drive('1XdDyravd7rul2GsSkwkUXZd3mUBgwGKJ', dest_dir, '06376.zip')

print('Dowloading dataset : sculpture, sequence id : 06377')
download_file_from_google_drive('18j6p7pvlLjn7Cwzpv1L3YXI79LiBR4KZ', dest_dir, '06377.zip')

print('Dowloading dataset : sculpture, sequence id : 06378')
download_file_from_google_drive('1zIkolfGaz2prrtmvrR7Ucj3fL7Pntp-_', dest_dir, '06378.zip')

print('Dowloading dataset : sculpture, sequence id : 06379')
download_file_from_google_drive('1IcHNqp3AdnXpIrEwNwN9mLeMHn0xgHYV', dest_dir, '06379.zip')

print('Dowloading dataset : sculpture, sequence id : 06380')
download_file_from_google_drive('1cDXtVv2cIW361oKRXTbP0wkDE9oHC0Qp', dest_dir, '06380.zip')

print('Dowloading dataset : sculpture, sequence id : 06381')
download_file_from_google_drive('1WBngLGgreBk5etgUe70b0qYhnl2FL1AQ', dest_dir, '06381.zip')

print('Dowloading dataset : sculpture, sequence id : 06382')
download_file_from_google_drive('1DIxTB8cO2drW3TblE0gPrP20zgfJFNDa', dest_dir, '06382.zip')

print('Dowloading dataset : sculpture, sequence id : 06383')
download_file_from_google_drive('1C9gPaEWV5qSvgCTxw48-Y4WDuAFDmBPq', dest_dir, '06383.zip')

print('Dowloading dataset : sculpture, sequence id : 06384')
download_file_from_google_drive('1b9t0ONskOGw_BpkLjHokAnWoKr1iAK_H', dest_dir, '06384.zip')

print('Dowloading dataset : sculpture, sequence id : 06385')
download_file_from_google_drive('1CDeX6kc2WZPqI-4pwtTbmxb-gVIStYdZ', dest_dir, '06385.zip')

print('Dowloading dataset : sculpture, sequence id : 06386')
download_file_from_google_drive('1UxbcY_rDcogsd7eGXhX-NaukCaDQNeBu', dest_dir, '06386.zip')

print('Dowloading dataset : sculpture, sequence id : 06408')
download_file_from_google_drive('1H-dareNpT1MVCj53N3BC4Rw-GUUIf2tw', dest_dir, '06408.zip')

print('Dowloading dataset : sculpture, sequence id : 06480')
download_file_from_google_drive('1-DMblLmv31rost-I9VXKCkEWn9uX3d4G', dest_dir, '06480.zip')

print('Dowloading dataset : sculpture, sequence id : 06515')
download_file_from_google_drive('1qGkL_MDhbXNd-7w2PN51ZXkULhsmfPIM', dest_dir, '06515.zip')

print('Dowloading dataset : sculpture, sequence id : 06746')
download_file_from_google_drive('1JPFuBlVaiqrnaAoVeg1219-2Oep6frNm', dest_dir, '06746.zip')

print('Dowloading dataset : sculpture, sequence id : 06783')
download_file_from_google_drive('1dQk8zqBWHSScEclA9V6bDZEIiThRQRFK', dest_dir, '06783.zip')

print('Dowloading dataset : sculpture, sequence id : 06784')
download_file_from_google_drive('1vJ7Epmf-do0dqhUiIDjXVzH0dluvpu82', dest_dir, '06784.zip')

print('Dowloading dataset : sculpture, sequence id : 06786')
download_file_from_google_drive('17XGP_8KM7laiXHiUyY_ybE175fLnv4oM', dest_dir, '06786.zip')

print('Dowloading dataset : sculpture, sequence id : 06787')
download_file_from_google_drive('1wgQhZCRPcRIcUy4s1n-IdSe19oN1O9uF', dest_dir, '06787.zip')

print('Dowloading dataset : sculpture, sequence id : 06788')
download_file_from_google_drive('1bkwt-avSmkHkp7q8lBTiFAydxlJRM82t', dest_dir, '06788.zip')

print('Dowloading dataset : sculpture, sequence id : 06791')
download_file_from_google_drive('1MQLAOTBtXLkR2YV8uDAGdrTRcB0S1Vnl', dest_dir, '06791.zip')

print('Dowloading dataset : sculpture, sequence id : 06802')
download_file_from_google_drive('1qbq9h6LOe4Lb2_Zn9H6-vRAqdZY21IXu', dest_dir, '06802.zip')

print('Dowloading dataset : sculpture, sequence id : 06803')
download_file_from_google_drive('1YbQlAudmyBTzvAg3YmFfp5cYiL8vj21G', dest_dir, '06803.zip')

print('Dowloading dataset : sculpture, sequence id : 06804')
download_file_from_google_drive('16KpCBZOU5VVPNmHvs1w-AgTy0SisLMnF', dest_dir, '06804.zip')

print('Dowloading dataset : sculpture, sequence id : 06811')
download_file_from_google_drive('13LhMzjyJGn_oIKFh4I4s94YMoIvGcVV6', dest_dir, '06811.zip')

print('Dowloading dataset : sculpture, sequence id : 06813')
download_file_from_google_drive('1Hd2xKYPAFybij9y-Lshz_rx7oxcxVm0l', dest_dir, '06813.zip')

print('Dowloading dataset : sculpture, sequence id : 06818')
download_file_from_google_drive('1oFIYIuizUInNss3VSc6B276V3d1Y0Yff', dest_dir, '06818.zip')

print('Dowloading dataset : sculpture, sequence id : 06819')
download_file_from_google_drive('1GqhLx8Y-L8eefeSHWDgpdl-axDdeR3t9', dest_dir, '06819.zip')

print('Dowloading dataset : sculpture, sequence id : 06820')
download_file_from_google_drive('1kRlC6RWTbfV5qt9r7hpqxFi0iQMmG4Qi', dest_dir, '06820.zip')

print('Dowloading dataset : sculpture, sequence id : 06821')
download_file_from_google_drive('1R6ybDCZTXabJyn_8S80azMej2WXZlB9_', dest_dir, '06821.zip')

print('Dowloading dataset : sculpture, sequence id : 06962')
download_file_from_google_drive('1HtRKt3rtUEbnuRcqbsxN2yTAIjyGwrH8', dest_dir, '06962.zip')

print('Dowloading dataset : sculpture, sequence id : 06964')
download_file_from_google_drive('1Ahy_hv2BEKRXJZ7dAPLOD86sOoI0y7JD', dest_dir, '06964.zip')

print('Dowloading dataset : sculpture, sequence id : 06965')
download_file_from_google_drive('1OEBvzzQOI1Q9x80iyA2I5qbzEE4Gzd1g', dest_dir, '06965.zip')

print('Dowloading dataset : sculpture, sequence id : 06977')
download_file_from_google_drive('1P6dvdIIRI-bBnke5mjk3pIPqUhRLbCOa', dest_dir, '06977.zip')

print('Dowloading dataset : sculpture, sequence id : 07027')
download_file_from_google_drive('1QNA2XuuJK_jaMFfnBH4vCNshkS9qFFcr', dest_dir, '07027.zip')

print('Dowloading dataset : sculpture, sequence id : 07028')
download_file_from_google_drive('1JtGK63quIfJw5SsYos3pwaPS1Gxtcs7F', dest_dir, '07028.zip')

print('Dowloading dataset : sculpture, sequence id : 07254')
download_file_from_google_drive('1TQuzl5z_FGHsQTTQT_lFsq923riJ3x5z', dest_dir, '07254.zip')

print('Dowloading dataset : sculpture, sequence id : 08922')
download_file_from_google_drive('1fFs3nw2znBJ2QS7Pqk2sQTicPD7c5uih', dest_dir, '08922.zip')

print('Dowloading dataset : sculpture, sequence id : 08923')
download_file_from_google_drive('11qLqTnIR0yXswJeMQyLBZ0pFzuBrOXzS', dest_dir, '08923.zip')

print('Dowloading dataset : sculpture, sequence id : 08925')
download_file_from_google_drive('1IySuiuzPEWTzeOfb6eRclw17peJ6kF_6', dest_dir, '08925.zip')

print('Dowloading dataset : sculpture, sequence id : 08926')
download_file_from_google_drive('11mjNKrcaovL4ZQdEyfszMs7rUFH-6sOE', dest_dir, '08926.zip')

print('Dowloading dataset : sculpture, sequence id : 08941')
download_file_from_google_drive('1iUhWoE_OsU64kJTOjGLberqKZ9wb6c6b', dest_dir, '08941.zip')

print('Dowloading dataset : sculpture, sequence id : 08942')
download_file_from_google_drive('1Nd_PgiTE2lUHk-0apZ6WWeh9KvyevHlB', dest_dir, '08942.zip')

print('Dowloading dataset : sculpture, sequence id : 09129')
download_file_from_google_drive('14_dUlEzOWIJMYFZr1bUywhD26ppGS8N3', dest_dir, '09129.zip')

print('Dowloading dataset : sculpture, sequence id : 09247')
download_file_from_google_drive('1sUMH5vmLzdPgrfAJCt64dgYYfH1OerfG', dest_dir, '09247.zip')

print('Dowloading dataset : sculpture, sequence id : 09250')
download_file_from_google_drive('14JkXgUqon7bpivxVyhNJE2mxK2kM6xFd', dest_dir, '09250.zip')

print('Dowloading dataset : sculpture, sequence id : 09252')
download_file_from_google_drive('1U62EED2knR5X1Fc0GAzovAj5b0qD575b', dest_dir, '09252.zip')

print('Dowloading dataset : sculpture, sequence id : 09254')
download_file_from_google_drive('1onmDSGIGj1eKY40YKrjRTCSOaMhg00vT', dest_dir, '09254.zip')

print('Dowloading dataset : sculpture, sequence id : 09260')
download_file_from_google_drive('15oBRJkhGBTCffVfeOi5TJdbST5gt8Bzq', dest_dir, '09260.zip')

print('Dowloading dataset : sculpture, sequence id : 09265')
download_file_from_google_drive('1nAeyaEE758rpX9UUCBfev-5t1676meco', dest_dir, '09265.zip')

print('Dowloading dataset : sculpture, sequence id : 09266')
download_file_from_google_drive('17X8XBjWSQpJBl2gZsCgEr2ZTZu3LQ9jU', dest_dir, '09266.zip')

print('Dowloading dataset : sculpture, sequence id : 09274')
download_file_from_google_drive('1Jtm6io1KjEXTTuto1PMLJPUaW-VJ-yXk', dest_dir, '09274.zip')

print('Dowloading dataset : sculpture, sequence id : 09276')
download_file_from_google_drive('1dYyxibnNZsRHMYhXZhsaPT9anDohdd0c', dest_dir, '09276.zip')

print('Dowloading dataset : sculpture, sequence id : 09278')
download_file_from_google_drive('1nmGabqBZ3nDB0oX0jSKQFZejNokSAgzL', dest_dir, '09278.zip')

print('Dowloading dataset : sculpture, sequence id : 09279')
download_file_from_google_drive('1q-x6M7IC69VPFUW5P6Ni4nphvZbkj5Sv', dest_dir, '09279.zip')

print('Dowloading dataset : sculpture, sequence id : 09280')
download_file_from_google_drive('17kox5jkNJXijgs0v0IladmD2TLIXYVcj', dest_dir, '09280.zip')

print('Dowloading dataset : sculpture, sequence id : 09282')
download_file_from_google_drive('1QOpFh-RVG96Jh204AwkZ0esafPpFxQzt', dest_dir, '09282.zip')

print('Dowloading dataset : sculpture, sequence id : 09288')
download_file_from_google_drive('13Rfr-D1LbjWdhefFxnA8H0LDq0UqgHYs', dest_dir, '09288.zip')

print('Dowloading dataset : sculpture, sequence id : 09289')
download_file_from_google_drive('1q-WZ787dDcCjSX2qF0z_da-gPEcclozo', dest_dir, '09289.zip')

print('Dowloading dataset : sculpture, sequence id : 09290')
download_file_from_google_drive('1_yJteO3wW-JxAU8zIAw3NWjyaYMBxRem', dest_dir, '09290.zip')

print('Dowloading dataset : sculpture, sequence id : 09291')
download_file_from_google_drive('1ghFAMUmYwtFPU1vZcEKNy89vRm1bOZXb', dest_dir, '09291.zip')

print('Dowloading dataset : sculpture, sequence id : 09292')
download_file_from_google_drive('1oFvYQmILcb2pgjaIIfic979eVVeYBprh', dest_dir, '09292.zip')

print('Dowloading dataset : sculpture, sequence id : 09294')
download_file_from_google_drive('1ciOivz__2BdWa7zI5ZYWqou8wqhfwdtb', dest_dir, '09294.zip')

print('Dowloading dataset : sculpture, sequence id : 09295')
download_file_from_google_drive('1lZxaBsWNwSATik6X7NJ9essp2RnxRXrM', dest_dir, '09295.zip')

print('Dowloading dataset : sculpture, sequence id : 09333')
download_file_from_google_drive('1AtkVcEKoiueeeTp7-R41RfAUCxzWXU5r', dest_dir, '09333.zip')

print('Dowloading dataset : sculpture, sequence id : 09334')
download_file_from_google_drive('1hFyJbRZhiTps9AY_InISIPkXqsaP03eg', dest_dir, '09334.zip')

print('Dowloading dataset : sculpture, sequence id : 09335')
download_file_from_google_drive('1q6aeKFo8YBD498PRdQGnfVoqTzp6w3nw', dest_dir, '09335.zip')

print('Dowloading dataset : sculpture, sequence id : 09336')
download_file_from_google_drive('1gaCDiYnNi8bhzjaycKVRJI89775KbGNW', dest_dir, '09336.zip')

print('Dowloading dataset : sculpture, sequence id : 09337')
download_file_from_google_drive('1uzho4d32DpCncnG6DD-t1bYA9L2gJSJC', dest_dir, '09337.zip')

print('Dowloading dataset : sculpture, sequence id : 09338')
download_file_from_google_drive('1a83s8_W-AzEExQyNkxtWqgk9a00srRMH', dest_dir, '09338.zip')

print('Dowloading dataset : sculpture, sequence id : 09470')
download_file_from_google_drive('1SOeUG5c7d-O28ac1aGSirOgfD0DsqPLO', dest_dir, '09470.zip')

print('Dowloading dataset : sculpture, sequence id : 09494')
download_file_from_google_drive('1ygJd7y3xucAudyGotODhFDcStHSMmhjB', dest_dir, '09494.zip')

print('Dowloading dataset : sculpture, sequence id : 09523')
download_file_from_google_drive('11XkFnCdVRpu84wQZLnGTyli5w-T-OuIC', dest_dir, '09523.zip')

print('Dowloading dataset : sculpture, sequence id : 09570')
download_file_from_google_drive('1r_SFEcsX94sf_GxJ4b9iNBnqO0RBZAUn', dest_dir, '09570.zip')

print('Dowloading dataset : sculpture, sequence id : 09571')
download_file_from_google_drive('1re3gLT-cMHtCdCXFTTN0zOygbFELxZ33', dest_dir, '09571.zip')

print('Dowloading dataset : sculpture, sequence id : 09572')
download_file_from_google_drive('1wLLkAIUQpN4e690NGhhEp1oryDE8t-5G', dest_dir, '09572.zip')

print('Dowloading dataset : sculpture, sequence id : 09573')
download_file_from_google_drive('1Cjjfi2wSVXrxNSrn3RlP9VHrpP4xjxpu', dest_dir, '09573.zip')


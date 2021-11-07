# 抓百度翻译案例
import requests
import json

if __name__ == "__main__":
    post_url = "https://fanyi.baidu.com/sug"

    data = {
        "kw": "hello",
    }

    # post_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 's',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '926957.706524',
        'token': '256332c05a7b593759523347e53eb1c6',
        'domain': 'common',
    }

    # response = requests.post(url=post_url, data=data)
    # print(response.request.headers)  # 被反爬，所以需要ua伪装

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Cookie": "BAIDUID=34C9710BC36816D0D21C829643DAC113:FG=1; __yjs_duid=1_5ab1b57eb734e88a9aa6439bd53a11d51632976979341; BIDUPSID=34C9710BC36816D0D21C829643DAC113; PSTM=1632978103; MCITY=-%3A; BDSFRCVID=Ay4OJexroG3VPY7HS5od8ggOj2KKv3JTDYLtOwXPsp3LGJLVgVCoEG0Pt_ZYMak-XolpogKK3gOTHxKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJk8_DPbJK-3fP36q4cBb-4WhmT22-us0G7A2hcH0b61Jb6Jebojy-4E3fTJLhJk3DviaKJjBMb1DbRkqq-b2J08ygc9JMopWDTm_q5TtUJMeCnTDMRh-l04XNbyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuD6tBj6vyjN8s-bbfHDj80n75ajrjDnCrjJ6OXUI8LUc73-7ZMItfan75Wt3MSUOXQ4JvyT8sXnO72P7T-HTp2pO82ljMV56Ky4oTjxL1Db3JKjvMtg3t3fbwBKOoepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEJRAjoK-XJDvDqTrP-trf5DCShUFs3RFJB2Q-XPoO3KO4VMI6yh-hhP3bbUJ9ajjiW5FeafbgylRM8P3y0bb2DUA1y4vpKh5ma2TxoUJ2XMcZ8Jjcqq7ohb8ebPRiJ-b9QgbOahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj8ajT5b3H; BDSFRCVID_BFESS=Ay4OJexroG3VPY7HS5od8ggOj2KKv3JTDYLtOwXPsp3LGJLVgVCoEG0Pt_ZYMak-XolpogKK3gOTHxKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJk8_DPbJK-3fP36q4cBb-4WhmT22-us0G7A2hcH0b61Jb6Jebojy-4E3fTJLhJk3DviaKJjBMb1DbRkqq-b2J08ygc9JMopWDTm_q5TtUJMeCnTDMRh-l04XNbyKMnitIv9-pPKWhQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuD6tBj6vyjN8s-bbfHDj80n75ajrjDnCrjJ6OXUI8LUc73-7ZMItfan75Wt3MSUOXQ4JvyT8sXnO72P7T-HTp2pO82ljMV56Ky4oTjxL1Db3JKjvMtg3t3fbwBKOoepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEJRAjoK-XJDvDqTrP-trf5DCShUFs3RFJB2Q-XPoO3KO4VMI6yh-hhP3bbUJ9ajjiW5FeafbgylRM8P3y0bb2DUA1y4vpKh5ma2TxoUJ2XMcZ8Jjcqq7ohb8ebPRiJ-b9QgbOahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj8ajT5b3H; BAIDUID_BFESS=34C9710BC36816D0D21C829643DAC113:FG=1; delPer=0; PSINO=6; H_PS_PSSID=34649_34532_34068_31660_34599_34584_34505_34107_34813_26350_34761_34627_34791_34694_34681; ZD_ENTRY=bing; BDUSS=Hk2R2dTdVlTcXIyTGNxTXNTeXJpQ0xZTFlteHo2ZmhkYVo3M01FdnVyVDhYbzVoSUFBQUFBJCQAAAAAAAAAAAEAAADSmXM5xsbP~jQxMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPzRZmH80WZhO; BDUSS_BFESS=Hk2R2dTdVlTcXIyTGNxTXNTeXJpQ0xZTFlteHo2ZmhkYVo3M01FdnVyVDhYbzVoSUFBQUFBJCQAAAAAAAAAAAEAAADSmXM5xsbP~jQxMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPzRZmH80WZhO; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a03842131211klEyq5b3cZvLZDjRLcXYYJ222DFbaumXAAWW5ewLACWZPoD7K%2BPvxuuAWtobRyJvprzOY3Zdagleo1ut8pfi9SbKXnH0Wc17pCvte2cgKugDeX9htqOsfKoOTY9OQVbRQuMu8Uda%2F%2FCk5BMwyg0wZwGhaDVPzdPTl4tyA8oD%2BntAUz5Udsn1x7Vc5ojLA1YUaWSNy25cTB25tMS8hqGmuQW8kIydsCYmbhCAUphHqL4bRMjO33hCdP2x0duXHR3KX1uQGiNDJrCPV5rGCy0jA6mcovLaU61TZu%2BYQg6wOcs%3D48594444660351331086537215236193; uc_login_unique=0fe2b66cb6df3f2158dfd200f9434cd7; uc_recom_mark=cmVjb21tYXJrXzMyMDI0MzM4; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1634630916; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1634630916; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_st=2_YzExMThmZmNkYjRkZTYwZmE4ZjI0MWRiZDM0NDJkZjJjM2M4MmNmYTNmZjUwMzUxMjI5MTZlN2YxNTNlN2JlMTE0NzdjMWYzOGViOTMwODA0ZjM5N2Q0M2FiNjJkMTgxODVjODliOTJmMjRhYmQxMWRlMWY3MDBmMjZhOGUwNTUwYTY4ZTQxMDFhOGUxNzc1ZWQ2ZDg1NThmYTU5ZTAyY2RkMGNjNjQyNjJjOTJjYWRlOTgwN2U4ZDFhNmVkODhhMGI1OGU0NTNjNDA4MzM5ZWNkYjJlYjcxMGI2YTkyZGYxZmEzMDI1NGVmNDBmM2JiZGFkMTczZTA1Njg2MTliNV83XzkxYjZiZTY5; ab_sr=1.0.1_NWM2ZTQ2OGYxMGM1ZjE5OTZlMzJkYzljNDkzODQyOTlhNGUzNmQ3NjkzMWIxNGY0ZGZlNDQyYWNjZjYzYjc4ZjlmNDUwNjc3OGYzOWQzYTY5MTZjNDY1ZDlmOGEyYTk3Nzc1Y2ZmNjhjZGI4MGQ0MTRiYWE1ZDE1YWE1YzFjOTc2OWI5MDAwNDczODc3M2E5NmU5MzA2YjU0NjNlZmEzODQ4YzI2MWU2NDlhNWNkMWJkMWU4Zjg2ODBmMWUyYTE2",
    }

    response = requests.post(url=post_url, data=data, headers=header)
    json_data = json.loads(response.text)
    print(json_data)


# AI-Powered UML Diagram Generation Assistant

## Description

Modern software design relies heavily on UML diagrams to communicate system structure and behavior, but creating and updating these diagrams manually is labor-intensive and error-prone. This project addresses that challenge by providing a conversational AI assistant that transforms **natural language requirements** into fully rendered UML diagrams. By integrating state-of-the-art **large language models (LLMs)** with tools like PlantUML and Graphviz, users can simply describe their system in plain English and receive professionally formatted diagrams in response. The assistant supports iterative refinement: users can ask follow-up questions or request edits to continually improve the design without starting from scratch. This streamlines the software modeling workflow, bridging the gap between informal requirements and formal UML representation, and ultimately improving design efficiency and accuracy. The source code is available on [GitHub](https://github.com/1235357/UML-Diagram-Development-Assistant).

## Features

* **Natural Language Interface:** Users describe system components and relationships in plain English. The assistant parses these inputs and generates corresponding UML code.
* **Multi-Diagram Support:** Initially focused on class diagrams, the system now supports **sequence diagrams**, **use case diagrams**, **component diagrams**, and more, enabling comprehensive modeling of software systems.
* **Iterative Refinement:** Maintains conversation context so users can request incremental changes (e.g., “add a new class inheriting from Person”) and the assistant updates the existing diagram accordingly.
* **Syntax Validation & Auto-Correction:** The system automatically checks generated UML code and fixes common syntax errors (for example, correcting `class Child <--(Parent)` to `class Child extends Parent`) to ensure valid diagrams.
* **Multi-View Projections:** Users can view different aspects of complex diagrams without full regeneration. For instance, switching to an *inheritance view* or highlighting *associations* across classes, all enabled by the **ProjectionManager** module.
* **Persistent Session State:** All interactions and diagram revisions are saved in the session, so the conversation history and previous diagram states are retained for seamless multi-turn design sessions.
* **High-Quality Rendering:** Diagrams are rendered in web-friendly formats (SVG, PNG) using rendering engines (PlantUML, Graphviz, Plantweb) for clear visualization. Users can customize output format and styling.
* **Save/Load Capabilities:** Diagrams and session histories can be exported, loaded, or versioned (planned feature), supporting teamwork and documentation.


---

![](https://img.plantuml.biz/plantuml/svg/bLRTRzis47yteF_Xa3vqVKYNVcsDKGHrdRKBq1R1lEwTaKuo6uhKI2gUD_H_tnr5onJjpjXBOjxzxll7ezuwBwplMmLdNpvzX6if6YjQkCO7LAPhKNjOE2S9HR_EIUw5L5Z15uUm5FGdMfmLisBs65P-gn24hi2liKLmwBtKZIjcxbxgJh3lKWdd5jvRUTTxl2cDNic_4IuECE-DzeF3EwEg0_KxKTutrlIwMXfbB3ogB-hNTNs8CxP26p7FonVuQXAg8pUYmQCeBkaQQwcffj8RItM4_zGiX_OCX8EUVepIZq8tFJc3JwP21OlRcu1HgeL7IZPhVwTw7D6xPl-6ca97VpOUea5Z4NNixTPvRAaNLB6mss9ciQInDDIVqxCxWt-A6S1ZkBMo9MlO67jVAxFX0g2aIJhumU6VFLb9ePumc3Ii8E_BPtDO6btBfhV8PS4g3ZRaN0OLYJEhvtF2ASeIfeq9HYvemZapUq71riB3HlerB8OMbYJ8O2_dy04rMk4Halg7b9ge8KLczceEl_pbBSrWxDYIaWXME2Zud5dzD8zZceOPfXL5cSdF5AYInwAGzBZ9wpaikavjHvjRQxvIbwJHGpp1shqmCx-aVei7dAReI9946rYmGfePisW__dpY5tFuG-A6v_w0rWcE1xyIcupT1iSFf8tdt9RfOf47ypdp42mrRb9PRasqUMziImpWHR8qbeb-sCOwO8xCwXaHY7fKedEqa2YFbfXAutCTjH67hdI3Vb3dzYzvs2KjX6dnryABE7LMyZ6t978jgg-zyt43tFAAGKykXl45NH0Uz9iOjYB6bsjuXtv3jtwicCSGPna0uLpClWrhOH6MYKKLadHhsRdXvYIJvIK5v-VfHTs99jTmn8NRjZjD-BeJ7Z1nfvZGOeoIad1qCUd6Jdf0Zj57MdmnuwKwfXeFariVPTcaUMt63KlAxFwcgfHUtESRNQg-mXzfHn1gsl1YDdOMdZwzIfiAStZpHWwsLrS4vCt6c2JNxs8ckNyNjQTZ3abZC3BPRpaqLGrEaywS0kzxTO3SS-T_8lypWOnzfmtIYJ0uvLx03cDbQ4BW4-rDM7qw0-RGP-EHNvbE2QbvAT5N4WolRaaqqwG6RpemzVHD_PrWVjl9KgZzmns-tE9TPn3jaB0m0scmSkISlewQDIakgRsaOV-SI8XZ-VCYH8fFApsyv_JGKHMTHSTV3vmTrOx1VHNBYfpYhaTw7d5-PxmtBNi_ycBHqqY1BfD0fcET21y2DdnljOCuHif2lAK3VR8Mity1)



![](https://img.plantuml.biz/plantuml/svg/bLRBRjim4BmRq3yGxg6Fm47Qea2HGn4tGOi02H3Kw5bWg9NCXYO9adBY1ldtBgs7AObIdOljQ6TtPuUpL2wieyQL6q7clszlo1MdXQ4RSWLR44flG3goj9OZ2dyjo59IiSC_oOq7p9DPCdjBLcudW52P4RU63H0Bpd5Ps6Hc7xZKr1TaWbgxTCxm-zB1DLDonVy2EHjWVYZfgeBtIcI3y7VA7WgZIfbTAg4CUPEVvL_pV8XJ9WDJOpwnp_2bqqfZ6Lf059NCwkWHaip9Sp8ZLKk2w1hy4oGOwhYIIwqh224BoXpVGYgeB4eidsvK1g8RuzA1qGRmimxiGUcUjNzgwyS1S10yiI20kLwZT--xqQoY6hPi8Tee1jQcfVNbZTferyRWoHaQv3CitWODI1IqYRMFcG1g42ctI7AlIxf60PNPLP0N_t4GygOcVkjvBpM_5DohtjEn8v_cAItHVj9nLZLuW5qGH5vQuQYJgfvmoHsd0fqv9jwKCg-SilRAzK7__eH3DqmUUy1-wb2Z1mTFm70nss3HEZZA_SweFsWY3DzIYIe5rBUK2telmAjJOnhJijAWGLmGgRjJhSKkUDpIAi2bqOfHLfU1z5VKqHLgx_UuuIPKWGCQB85dqd0AZyi3SYuW5kEPDrVEsxDefjcWgDueF6jyO82Yb18UEsO8beJXlHErK1tgcYyrO3NE37rOw0QysSf1dH2WIjSYUhgjS08ak798ktUU9yzup-5ElP30NVwucZNpuGEn5asph1N6gOWEKoj_LpbLHLX4zYzzv6xTMzCMlyRNae2EvzCCzM2ZJ8PhUGITflwUoc3vUXsM1_dkS6GxB5jVesnDSLaGCfohGIYPywAiDdKQsb24ZAFz0oooUwbUvBz0x0lPDTUuisFli_d7EVcmMEo_HwxgSuBC7ENoo3AHk_2r9SQMFwoJp2ADJa-_HUwpSu8MmvGHO_gaCLP7fCOshacRCk0nRV-NFzKxcGtCUKpBQD9KdsZ2Y5wJELF37eQwm1N0_t7_0G00)




![](https://editor.plantuml.com/uml/bLRTSzCu47_tZF-7dV80F9JZet3N3DCXjC0nGpiTSl2ksXj785j6aXioD_plx4gA8olXohsqqUvlltzQ-PLrmhYXLN3qwV83N4ZH6D721TwYqdsBdOEvjP9GzEkOv4v8XJLyiWZdWlv4YwEoA8lxf5_A3a5KJXjR5lu_URPeZa1O6EZ7AFqWkcOG3SAbhb71_FgznoZLmZqbcvMxKGEEw6rc7x6hqKH_9XwYGMCGkv38OcCTjd2ZXwuMPbCM1YkgeL7u6uKUmRzb0N0VherioHhMsdnTAhtc0g2YiYqyiFXj82ifr4C6auOLvFtyoGpETRUKpM2Gou85EYUxnlgSAwyYSMRrT4OuHLd2j37Uo7gDFsTcpoZOIZXOIxU2UMXXHO8CTZA3TzYX4GuXgJ-ar4GDAJApvpDuyzqPci7OiNDAmbjXKF0vitenYsEQXWdJYgBCv4yALCj3KKXwsEIl6SpxNcr6cskZlr2NfEv2FC7QdJ0pFwL-YrkSfcX9aaGBB5WWpOnPj1j_Fl77C_WiSSrplqLZ1SU3lubDscoyurlIndDkotGno8EvoZnuomxNgIot9jgyrQOb1eYk9cl3HDzluz9Z3ipg2H68UbIXjR1mb4TBJANnsPxQYA4hVT07TMv_miEkjAcdnLy89-BKMSd7t9B8DQ-_3DR53N0jA6Lqv2ACp-kySA_VnB05CRvQmMjqQxhrOyKyXZXB3_3dilWHriBSBnE3oYTfLxAtuUOaa-Kb1SV7wKNTYYRNSCJvsxOzJVYw5UunSQkOq6ACaf9mT37fnbQwHuxHHrfyMV1I7LEDXycjZx9iqhmsuuObPNP_KrLAB-xp-wvIGur_q8uWrBJXPJ5s5XuzEakR2ZDu-L86sxCp0l9cOqoIwoynazn_YThHCOUaCHYPxBSScgg2qwGpTu5tlTf3xhZpFv7_cK36lhiDqeamEEMUnuQnCZGXy1tjJLXzTmRCeIlja5-PNWdPyL9oAuJmwbP4iuxKu7GFUZbzK_yXcDlqiX9gzt3xpvnurnb4EyGlJ4yQh2qvDtfeLgGufVQIXlrp8ZwEuSyB7oa-hVJm7jD3HrNq1Yr_FN1sL3jwztKiAtAAknxfUS3vZNPEj-pzm8j5JoC5Eaq2wPvrmdy86F-zrGPnZ9I5U4K7-huhYvy0)




![](https://img.plantuml.biz/plantuml/svg/lHhDRkCs-XuWxq2aX_5qdC5qjmMsGJke9-Dc3DY9ONlci1U1bcYR3IKA8cLFMiojBr2WsEjU-e3x2FjHf6nI8cLdVdf9BFBxv_TBwISXSI7BbA6BjvCnUatnki0fUassXF4y9Pb40o4eGC6lIrWNT9sXiTg-E3yxFtk2vlA14II8b3HR2xJY1Lh20obGGN22bvHH-N1-9kvfbcD5EsPOY86K1LsMaenYditfhmIzQC7yp3EfgIyvIrhRht1ylovucINNd07NhrOlLlzQhTfml4X8OM3-4V-JVEUmoe4CNfCZKBWe-2wuAq1TmkL3JgvRKk7lapXPALiPJkZYcXS4NVCqvnaOM5oWtyxFa1OMmIcOGxWX6Icmf3mRvBa6GUWIpBKbXQZM8o61qXMGEgoznXBFOHaO6Go6itK9Zr7A4yAYc55WUeN6PdcYLWSvlQxM3KwYHOXe1fhb1O6_LxLpZ0vh1Xh7acv9v3Aw0iyem2LS68UW0w2bg-ofTeNY5zVoM6WX49pdZCRQBc2a5LsNsdesrBC89A0oYdfFpGBZE8bA0NGTfDxJAxJbD35G0eFinw488x5isA6d5QD9hI_WlEAS4PovQ1wRzsozEoWedIXc44PDvgw05fpDnGNA2nuJ8RIwy93cikTu7Jn8ybwv4EI5FhBWB04NPSwC1puhI0pH5J6MHWKHuFM2zEeVDKeVaVSaBYi6YJ5lbC4HWw2kVC2wm9QzOb3K6Bb9zAdhOo181a5UO_Pi2WSvG9LVu3mg_k1e0PrYC7_b3GUxRAYAnmVRd1zKtDUXxO-uVMIR2Ea87gqapYdu0c3I5NrS52bCNCgDmZMHSayUchm02CoKSvf9pzOI2uY4eYcXvgliTKos-engSsatSa3M-ym7RgfSQmr8ek7qJN8uZikqP1XeEYJ3hXjA2U5eqf5A4lUG-gZhOEfT9t6qJgYF5BPr6dgXUH1zrBH_JRxXgbyqdWM8PI0YoIEUamnJOw8mvMuY1T7fctmY7SuOJh4XSbmLE0Umfq5I5cybg2ZUbDbzCvCqk2xf-f5YVqJ-QDVVPku8LzSJ2YZOQajZ4WZ-TfZeV4tsUVWGjP-KM0CrQXzw7Xtxg4kz4qFB7pHEaV6frP2-DaeEcKFko3BI9GSKyDk4P6kQaKYrZW6Aq52dM6g2qATtIk8Sc444k7opfR-UYEXut7H_OXESGHgq76wBASDBHgB3gRhk59S5w2wj_MCEfJgu1ml-qMxaajVaeFE045RQ467JvWK5osFM85v1Hal6u_kz-nI4LMujDZGN-s3sCQFPXXGKPgMOV75UWCjZge7_1iKWdbRuRr1Bq1GA0HJGvCknMXCPUHrOfLwhCr1mbhSbHCG5pIk1Jd529vG2Cze-e1XVGxA1JbdtH4xoTgg40bnHHfem9jmaJGbCwsaEze1gke177vLWasRIRxGZBERGpG4r0N86k9dTQZQX--aH4l6Myb9qJuG1ADCeXO339Su7uYNMpZmx25fIMHQKWWhi58i4JaixbriYD59Luy4IwaXwgLZNfb1vYgpeUyjPDQGzyC2pi1AZI__pJarMMVMwKsC8X61K7GwqDdi0OVozPHnjD9-9J4j03bxPQyPYN105a96T8rSlu7z-4_aSg1xHktjspqs1bqNRfrhqZpOcf_Ao6tL_1tlK1EqkLZUYRQzH9mCfBEDml3nBVAxZCG7DybA6cebkL5vA6rS_VffasirOxIkzEYlPEWVayYQxHYmaIkvKjMag3g9zsFPCHBTc0tLPLES5Y22T6jnCkKy7LUiN7SqLBkUGKW8ALkE248BhX5Y2KlN1kQ9yAwjxMtIjEoVdYd8EP83uND6k-y8VVb2iQFpoPLtHdlscLpuWA_NObtHQDbU5FGvEadrn0HCwgQ7WpEsO8PWDQCjkzOPfXbqimSiYLcF6Yk_3iUvWmpStKpqQy6wbFLDtjADoOoRJUdHqejAs3ir4rKTUXMw4MvU0UzORd2MCEADBf7nOjrB-cp8eLmpQkmrdwe8CKfgw-d-yH2VEhOypOQr8PJvx9lmiqWqEHAPmnA9J97E166_KHAOo1OZmADO-OesBeSz3jJOQIIXqb1z7jjd0Lc-1kWqqc4x7e-l1OdHt6or6Y_6mTZ3qumblc2wwoBqRpkRmtoQuVV7y-nREP3YV3sw6qUnkF8m6y_belXZSBcmq7EJduBwT3sSscWhbRepHxM8ucyw62nVHyjcsXky6Yy7i86SqkdPr_Dz___fF24j9w47uuwyGWYMW1-_FtoyyuK4XMhSmBwXW9LcP6bSvdFxTT7Wx6EdViw4-iA7P6ey7au7-_MfqCxbxFHo7yiC2SdE8nNGCfW7tqKytiy7qpRlHl-tAzGJDxC7l_2pq8ktYcmlqzULbzJzm8tzLrLyCeO9UdaR8SpNtU2AX4T6bv65b4sbVsRZevsU1OlRy-SlWoyShTIbSeNSW-zg20s9N4JYDzJ4AtVnRQVuqfbwqZ-0KiDiHh2wL3wXXxr8q3daxS8e7lm-1Urmk1EepJGYsMsuxyPmakHyX8BkTSso9djIVEDnoII2BPF0FIPuZlWfvYyf24mYlAioWDsN0GYSs2Mq2hCAaGJDSaKC8CuR4Wv0aXPtw2m047HlQyU9-nVZk_0mgE5ACbK2L00LTRwGIeHNTYcJbEg10GbShegvbq9QIdHePr2KuI8yKb6a8z1SQXrisW1MbQiuhTJoybrnAdYhc7PyPQ6a4oc4VIgkIGPZi1OXszwwWpOiECuCZFGAAVcK5fniINRO8Vy3mfcg0XJ9mMcOcgf1g7mysKd3ZyGGwZ950lRkSP8DH7zsC9vVVzg6Kc9THC8_A-FbJLuoVuA5CsVy1)




![](https://img.plantuml.biz/plantuml/svg/hLdRRkCs47qFa7yWt8UwG19ijoXGv66nRf8k32HD43Veey18jCr6fbIIiflz-Wvl4abHijojWNLaQUOCENFcGkrd8J6NpQv4ivU7UtHByORZ7RebUr9MzOumYHP2K922gqkq8dytXEN42SxEpyxFlaSh-LuI98YKb6t4-Pbuewp62aXOXGNdrU6FBStV6142VKp9VE5LK_zQyOBmJlB7OKcSlstWWXKtLLbnzDtwm_gNzJeb_m18U4CM9TqmlQSSlWXFYJw1EsXEQzZlfANuyjCNT4_Ny8yHOyAAVyn_8Zz_61K_Re5Laemkl1CODAj5UgRMQvmNgTNTqZq5k1EsxpHIor1yyfmARCAv187PYo1yXh10ZL2XgpiPD5lKTKbpB6d5dY3GmiZHI6e5pW29bSIIF606WWPGg1kHB6I3vVWNmWZNq615o-EwZgJlCTiqWFTG5QHyubKEbYe3NfQxziQOrgAcDoK5NZejyojIiMjQAlhMdC1tQAqmpuSizjMr5kr-Hme0z1V9rUPzXzNTtKsiSLEnFU52E-mMIxo2u86YTRI-ZZJk_W6x39Ve_lu1BPwMMfJOc-0MMsCiTyxF99LGRVnorOK8_LdnjtLP7OpIab590HbAKmCnK_IiaKSM9q2_wf_dPmW-Yb_eyXFmvnejSkL75N6dOcI0atGFhD4aqqfKgMWcNOC_BIh9FCrCFvt_425Ozgbx-X9TMjljsgmCscDEyMj9X94kI0h3NmuOlqOtd2WHHWveWDIz9Mc2wpjrRRQbunPW3SIvnJAQBOy3tJJn8rMFb85odyDEqTDG005B0uWUgmFJrltFm1dEl5WMVHfu8MXzrWL00Gcr-bigwXA_etoBfLabr5BIWr1S8gmmr0N_hkccuTQQfUxJCduGCzOz9bguwyaZhDKq4QG4bsIb3KssKx6Pw--C5iSOOY3mdcHgBLdkht6O4bwUH7PZUruzLFVRdzh9shZZ5D80VjXwVex0_A07pjKRwgktU-zxpvRVp6FYtBkUuCY0zPv_Q9_kBKPGldk9u9Re9SoeTtfem_vfwW8qZdYepGAjotT6jLgZl4_aeMHum9IXGrlQJJAaEq0_8rRDwuvALGvsjKHSzH6Xaa83s8YDveVVmgyLZheqH3UWsO7AhMMklIEXWLqeHoIOx7Ndhc3uzxrMWeiYsvdnDPELIgoswiwV7-_lifVL1GfiNbrTJMenuQxiYApiGQ6J5V8j7UytyUerunAUclkmQZTcpTu69lSYJdAO7mDmxxhl0Zjw62Ve7rrkgDco8uZ2JR0wW1WgQTFtFBBOuMhtoH-CWDgG8RhEMrP7EC4GvGMhgchq6mGAzhO5LL5NJ13eJWrxCnBguoaxlhXDhYJqqjsWPg8wssOASvy0UaNohi24ZBGg8qPI-VAYIrB0NgIo4-cH4qP1XsUGT8NfF3Eovni8L0b5CGBm-D7pzh0VygDW4GL6Km1aCmSqTnSNi1wIDvfpXIsofoM56iTRxq_BYj587jzqD4F58GvHjvWL9MbRRWxLDoi0NizrTd3fd07pLqwsLGa7Jhyi9-iM199Zhvihw0Xml4eDUS02GmPOQAIWJtD3E9tQSgEwcMZqMIN5fAZX96VJ8DewOqRNwBLdqurT9tw6kuJ3WlgD-DaKgHQOXw83tJS-qdOrriL7Trz_G4gqtVx1k7Dm_EoKzhlyVNh7xUyawBh7ksngePgnnfFE8NEVk1VUEIXZU3TCtU4vr5IIBjSsxRHrcgdUQ6cVbz8xaZcQE8Uep_Z9JXtBthFkvgH51GkBNcYuvy5j7SB0BLqEAgbaLaSHJTY9Eb2qqy1Up7jTb_mVwNDmWB6kr0IUGSepzThtFs4uEcYG0tdD3FqWyUmAIM5TFtDsPYdOU3Xmojf_2Cfxwr2wQrlCs4bbj4i6vp1MDp9QxMdDSQaGJkcAumkg6gbMr5P4U-FRc_YZnZbzg4sMgtOaq-4kmiFJS0CRgQ-3urhN8qHJndFjnEhglw8QFAjEAB9Xontgi-aEa-orhGDx9z2X0_1ZhJO1uojXCFVaHFylXkLlt87lEf5-3rOlFzzRxtRrwFWBej4UmyWXczfdlgd3J30q_ZharEunmM2Yga_h76jQIZ-HqgDM0lxaBk4i3PRu_xqM9rwbMkvEg1l9h8dLqPwImrZQV8Q_q7l-1G00)



![](https://img.plantuml.biz/plantuml/svg/ZLVBRkCs5DqRy3yGxcBQ01vCd-XgC8ha1W8anB3WReek69cIsT2aGD9EaoB_tikNJShAJ1PnoCl3otFVzXUbiTJ70qEBRLsXWk9UuWCgo8amCHm8roXJYW8ALajKuMSY0sendyrd7r2Zdnb1YcXDUQ_cC_L8-O2DbWVSFlPI7Fak5qn8zBIdciI00G2u9xSZt7VTf-xthfj22haZqgD-QdycltwQG3b6ahJ0kcV9YrXAyVJc_LOS1i71w7Smkc2_peaBFM5Wr-5sTmNxkYRADP5mxpt-kc3VvR4_1DSDVI7enz_UEhK-VH1ivwBkCc57Eigffe93u3qQBTQIA70CDd87N22iqBf2_yrdwE8vjCY6WT7M0jTmLLdSjhJh4RJHak03enhEKHxaxaQZj-KOJY1juNa0Dy24e1fpq6eosZ_IwFdirHXpvXsnYMXdrxIXL7mDt15EfBq1bnry6AQfM1gEXLFSDFK8MK6-7k6y5Zl2rbAqS5CuS5MlHs3Fe3IH7YI1p_H6KQx71XRYW6biMt5jMy8X6sZEQF1PLUVVvE2V7k60sJzGZk25s07hUaomv9t4IijZgu-IH4JBQwAvu2SYbNL-WJLkj92WnCBpeZ5eytVMlVeNw77CK4FaYRO-sLQDKvpweAfHjYuT0ZQm3gW4TpyGdfK6Qf7tMJa1sX2NLUICsqpYRcblVMvWwFkxgbx-yeE5tqx2xnd31tnvkmgeL_VlogZGsrUyfznRNwmcxLepQFTc7ZYi2zPsDO6yatZOd-XBZBpxSnKnUVKn3YtZt9cWmCzhAAaIbM7d2xHC075nGkYr5CpLMvxYd0zJNNKAYT9r11ozwLDg16fIq3clJDnIv2fBeHl2eHd3cFJk6i4tgz9v2kpZK2w9hw1xVlpusRa5Fc0OPzLybZcfTG9yWBG0QU6anco_DBVifHAEwx0etQ4no2yjOx-Ew8HuIy9i1DIU3ihmi9qQBPUVVG-E9Qx59XZJyMA1RPR0V1ZirZQviB7zAspipGiiZs6NjItx-GpKNBI3ckjDOIqhIhinRGYMncIRv7vjqzWeo-tM5dVOREBDRRnnTHXFIDLAElWHQQOyahJVQoGw68YcG6vkhkVbpOqvMQAjYYlcKdZA7Hj7Gan2KZ7HqpQvE1mrscE-Ot3i3ZP47Pb69wgEcD4N--Py1YhiDn33FEMOUOvNip5Gp0KqQXoTjWA-Sb3kDHj8cCNA3kB3UH1x8zpKCWOy2VdOCV6aWkgGTqAsUm9puPjq2qytddI1QPXiw61RX75hBoEQeK7Iq1ucpeRp85EH-Gz7PLgg2X5ucr_f-KqDki3J33Cqm6Y3hzs4jyH9apRp9lTBCX3Nvdq4da6LELNYADiq1Z7P3-vn4mF4y0DXoZURl_PqjoFyxsNSQo9XFI4pFQTEHOrlGv78TfacbQrS3Nq1Ql3Jv7y0)


![](https://img.plantuml.biz/plantuml/svg/ZLTDRziu4BqRy7yWqiF6XsAxkrXWuHos-V1s0oI14JS5UcJ4aSGDHMf9oeuB__ZEKA8-BANk8KOilXdEl7ap8tzqdbjV5OgTFTtViHl9CyiBTWDRKAOiG7jswPn45FxtdbqcNcwbtqVWsNmsd_t2DdwlW3dmNkhCiTHOzenVm38BNF1dgT1cFdClKfUS_4S_LpnvoQofjBWs2gtUfH_Ilz9q4cgi0Dl0Va_-W3y_l0txdClaHODpxBSf44PV62t6jwSfJyIFB7ukY07wH2mRAi19ZwisnWcCjMPtcXZ-TjmFniDFa15WKmoG1bffY4P3E-bpvdQoK1opdyyEJmxi0VrHmlFPyZ99Y9I-x5gfNP3FmsLPAfbmBur6k-Mjbbvo9Ry1uzq9GmCFQB2yHh5v88UDlq-WmGOGUc9Ia-iaGEyC5qn0oYlbMM9qAhEgHjOtDw4kDw0WyGmpo2gU0IkC07Kgk2dqaSF8aTJO9AK5_3pbzKsJw7f51u7E21NW4YlBm59fJL4IhyjDzLn8tpqOtVhkJcQvlr8LBAyWaxhrbxLyaZLLBvXZkx_CPumTxcBYzvGuMzSO70a7Ebu-GeBYOHN6szsEpzSMK5z0TTY2TVK5-CN3QuFOW1OuIlwlm7dc3KuQOX744TNiSdqR3EXlbqkSIUSRZweeC0QqTwNH3lvUCEdO-LTm2yA504AWBO8bUQLVBfhJfr84MTtMYiPGgIGjEC0mlkQ-1xE84InNhzxoX0HMb0eBraGvi8oij7TpJ1LU8Qa23GLuAnDtCV0Nwv6WkpPVcRBpBoWLCJZ6MOmTZIdx7FGWwOqto3dKBa6CdO9oNJveS6Uo2AV8KYvLPTlqPLe7Gc9WFEDI1qaWQ_zYHgeLmOrqfU9xTjQfummrBKX-njPvDemFz93ZO31sFrICQ9mHmKRZiYAYI2kr94VAVeEZbeGHJwqq1dYVuvpCygDMhCiGcm5pZrFjDi9Y687EVumjk0_btb98bF6e1eYZ3FRCxRNdhtXWBGJ-7HLS0mWG4RaAgW6KaiOHZKrsliR-y3WHVlraUPblvRT5Wwq_YOx70AR-S5KOo6cb9kI2xfjfsaMvbQwYsHJd9g6EHDCt0rnJ5WNj73PiX4VXTEHrua4AaVx_wdpPFTTeHsyaXoxwtdap7YQAsASn3ewoCqobYWKCoC-MQuUH55Fb6EU7uvSPAt5Eub2OieWfThfinaFJ-JqLqHJ0ZTIqUsoLffwjQ5kjnT6Fs2yITd4-Jo29gvg1Bl79eL2lfnuxVb_2G3H7BHNC7k5z7UHm-NTkeaHZIg1pMiN3GDiRshHYOesZ4Jupk0nk894ExrWRgVtKvAhtsLTGokoM4-XkUDL4uVQIQViUCqNJIk02nQVzDTP4Ks_NTVUSWY6l6xw57_cyCJkjmcj9ByKwaslSXL9NiEY5YtEkd-MeAjsWVJ3rW9dO2sU3TZoIr2DWWmzIZAyEDfo8_b7ldM74m1GlRHRTMw4fwVj7FC6V8zy1)


## Technology Stack

* **Frontend:** [Streamlit](https://streamlit.io) (Python) – an open-source framework for building interactive web apps. All UI elements (text input, image display, buttons) are built in Streamlit for rapid development and easy deployment.
* **Backend:** Python (3.8+) with [FastAPI](https://fastapi.tiangolo.com/) – a modern, high-performance web framework for building APIs. The backend handles user requests, invokes LLM APIs, and processes UML generation. Uvicorn (ASGI server) runs the FastAPI application.
* **LLM Integration:** Supports multiple large language models. For example, OpenAI’s GPT-4 and Zhipu AI’s GLM-4 are used to translate text prompts into PlantUML code. The modular `LanguageModelApiClient` interfaces with any REST-based LLM API.
* **Diagram Rendering:**

  * **PlantUML** – an open-source UML tool that uses simple text descriptions to generate a variety of UML diagrams. We use PlantUML to convert code into graphical diagrams.
  * **Graphviz** – for rendering custom graph layouts. Graphviz is open-source graph visualization software that takes text-based graph descriptions and produces diagrams in formats like SVG.
  * **Plantweb** – a Python client library that interfaces with PlantUML servers to produce high-quality PNG/SVG output.
* **Libraries & Tools:**

  * `plantuml-encoder` – encodes PlantUML text into URL-safe strings for server rendering.
  * Regex/pattern-matching libraries – for syntax checking and auto-correction in the `DiagramInterpreterEngine`.
  * Standard Python libraries (`time`, `perf_counter_ns`) for performance measurement and logging.

## Installation


# 1. Clone repository
   ```bash
git clone https://github.com/yourusername/UML-Diagram-Development-Assistant.git
cd UML-Diagram-Development-Assistant
```


# 2. (Optional) Create virtual environment
   ```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows
```

# 3. Install core dependencies
   ```bash
pip install streamlit requests
```

# 4. Optional: Add support for specific LLM APIs
   ```bash
pip install openai replicate llama-cpp-python plantweb
```

# 5. Run application
   ```bash
streamlit run UML_Diagram_development_Assistant_V1.0.py
```

   This will launch the app locally (usually at `http://localhost:8501`).

## Usage

Upon launching the app, users see a text input box for entering requirements or commands. For example, typing a prompt like:

```
"Create a class diagram for a library system with classes Library, Book, and Member. Members can borrow Books. Include attributes and methods for each class."
```

will prompt the assistant to generate the corresponding PlantUML code and render a class diagram showing `Library`, `Book`, and `Member` classes with relationships. The generated diagram appears below the prompt. Users can then refine the design by entering follow-up instructions, such as “make the Book class inherit from a Publication class” or “add a dueDate attribute to Book”. The assistant uses the previous context to update the diagram in place.

The UI provides buttons to **save** the current diagram (exporting the PlantUML code and image) or **load** a previously saved session. All conversation history is visible in the side panel, so past prompts and diagram versions can be revisited. This conversational workflow lets users iteratively build and improve their UML models without manually editing diagram code.

## Architecture Overview

The system is organized into modular components:

* **LanguageModelApiClient:** Connects to external LLM services. It sends user prompts and context to the LLM (e.g. GPT-4 or GLM-4) and receives generated UML code. This module handles prompt construction and manages conversation context internally.
* **DiagramInterpreterEngine:** Parses and renders the UML code. It validates syntax, fixes common errors (using regex-based matchers), and invokes PlantUML/Graphviz to generate diagrams. The engine ensures the output is correct and semantically consistent.
* **SessionStateManager:** Tracks all messages and diagram states in a session. It stores detailed metadata (role, content, source) for each interaction, preserving the evolving design state across turns. This enables true conversational continuity and incremental updates.
* **ProjectionManager:** Offers alternative views of a diagram. For a complex model, users can switch to an inheritance hierarchy view or focus on associations without regenerating from scratch. The `ProjectionManager` applies filters or transformations (e.g. “show only inheritance edges”) to the current diagram code and rerenders it.

Each component is implemented as a Python class (for example, `ConversationDataStorage`, `DiagramInterpreterEngine`, etc.), making the architecture extensible. Together, they realize a fluent interface where natural-language commands flow from the user, through the LLM client and interpreter, to the final rendered UML image.

## Iterative Development

We developed the assistant in two major phases. In the **initial prototype**, the frontend was built with React/Node.js and the backend with Python/Express/FastAPI. It could only reliably generate basic **class diagrams**. Sequence or use-case diagrams often failed to render, and a mixed Node/Python stack led to compatibility issues and deployment headaches. Crucially, the prototype lacked multi-turn context: if the user requested a change, the assistant could not reference the previous diagram, resulting in disconnected outputs. These limitations demonstrated the concept but showed that substantial improvements were needed.

In the **final version**, we overhauled the architecture for coherence and power. The entire app was rewritten in Python using **Streamlit** for the UI. This unification eliminated cross-language issues and simplified maintenance. We introduced a robust session manager so that conversation context persists across prompts. We also greatly expanded UML support: the assistant can now handle **sequence, use-case, activity,** and **component diagrams**, not just class diagrams. Diagram rendering was upgraded via the Plantweb library for high-quality SVG/PNG output. Under the hood, the new version organized functionality into specialized classes (as noted above), enabling advanced features like syntax error correction and multi-view projections. User feedback was used continuously, and each iteration refined the system’s capabilities. The result is a streamlined design partner: a tool that grows its understanding as the user’s description grows, allowing UML designs to evolve naturally through dialogue.

## Contributors

* **Yanwu Lang** – Department of Mathematics, Wenzhou-Kean University, China ([langy@kean.edu](mailto:langy@kean.edu))
* **Zhentong Ye** – Department of Mathematics, Wenzhou-Kean University, China ([zye@kean.edu](mailto:zye@kean.edu))

## License

This project is released under the **MIT License**. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Future Work

Planned enhancements include:

* **Expanded Diagram Types & Customization:** Add support for state diagrams, activity diagrams, etc., and allow customization of styles (layouts, colors, fonts).
* **Smart Completion:** Automatically infer and add missing elements when input is incomplete (e.g. adding default attributes or relationships) to speed up modeling.
* **Advanced LLM Integration:** Incorporate more language models and fine-tune prompts so the assistant better understands complex requirements and ambiguous user language.
* **Real-Time Collaboration:** Enable multiple users to jointly edit diagrams online with version control, supporting team-based design sessions.
* **Mobile & Cross-Platform Support:** Optimize the interface for tablets and smartphones so designers can sketch UML diagrams on the go.
* **Code Analysis Integration:** Analyze source code (Java, Python, C++, etc.) to auto-generate initial UML diagrams or suggest updates, bridging the gap from code to design.
* **Performance & Scalability:** Optimize backend processing and consider distributed deployment to handle larger models and more users without delay.

These enhancements will make the assistant even more powerful and adaptable to real-world software engineering workflows.



---

## 📌 Acknowledgements

> *This assistant was built for educational purposes as part of CPS 3962 at Kean University. We gratefully acknowledge the guidance of Dr. Hamza Djigal and the support from the School of Computer Science.*



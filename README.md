
# UML Diagram Development Assistant

A conversational assistant that leverages Large Language Models (LLMs) to support Object-Oriented Analysis and Design (OOAD) through interactive UML diagram generation, visualization, and iterative refinement.

---

## 🧠 Project Overview

The **UML Diagram Development Assistant** bridges the gap between **natural language requirements** and **formal UML modeling**. It harnesses the capabilities of Large Language Models (e.g., GPT-4, GLM-4) and integrates **PlantUML** rendering, offering users a hands-on environment to:

- Generate UML class diagrams from textual descriptions
- Refine diagrams interactively through conversation
- Explore multiple diagram projections (e.g., inheritance, aggregation)
- Edit PlantUML code and preview changes instantly

This project was developed as part of **CPS 3962: Object-Oriented Analysis and Design** at **Kean University**, under the mentorship of **Dr. Hamza Djigal**.

---

## 🎯 Objectives

- 📐 Generate UML diagrams from user-defined scenario descriptions via natural language
- 🧑‍💻 Provide an interactive, iterative, and conversational design experience
- 🎞️ Render and visualize UML diagrams in real-time using PlantUML
- ✅ Ensure model validity through adherence to OOAD principles such as encapsulation, inheritance, and modularity
- 🚀 Lower the entry barrier for model-driven development in AI, Cloud, and Big Data environments

---

## ✨ Key Features

- **Conversational AI Interface**: Natural language chat-based interaction to design UML diagrams
- **Multi-Model Support**: Choose among OpenAI, Replicate, BigModel (GLM-4), Ollama, and more
- **Real-time Rendering**: Convert PlantUML code into visual diagrams with instant feedback
- **Projections and Perspectives**: View diagrams from different analytical lenses (e.g., structure, association, composition)
- **Code & Diagram Sync**: Edit PlantUML code in real-time with live preview
- **Session History**: Auto-log conversation context and diagrams for revision and continuation

---

![](https://img.plantuml.biz/plantuml/svg/bLRTRzis47yteF_Xa3vqVKYNVcsDKGHrdRKBq1R1lEwTaKuo6uhKI2gUD_H_tnr5onJjpjXBOjxzxll7ezuwBwplMmLdNpvzX6if6YjQkCO7LAPhKNjOE2S9HR_EIUw5L5Z15uUm5FGdMfmLisBs65P-gn24hi2liKLmwBtKZIjcxbxgJh3lKWdd5jvRUTTxl2cDNic_4IuECE-DzeF3EwEg0_KxKTutrlIwMXfbB3ogB-hNTNs8CxP26p7FonVuQXAg8pUYmQCeBkaQQwcffj8RItM4_zGiX_OCX8EUVepIZq8tFJc3JwP21OlRcu1HgeL7IZPhVwTw7D6xPl-6ca97VpOUea5Z4NNixTPvRAaNLB6mss9ciQInDDIVqxCxWt-A6S1ZkBMo9MlO67jVAxFX0g2aIJhumU6VFLb9ePumc3Ii8E_BPtDO6btBfhV8PS4g3ZRaN0OLYJEhvtF2ASeIfeq9HYvemZapUq71riB3HlerB8OMbYJ8O2_dy04rMk4Halg7b9ge8KLczceEl_pbBSrWxDYIaWXME2Zud5dzD8zZceOPfXL5cSdF5AYInwAGzBZ9wpaikavjHvjRQxvIbwJHGpp1shqmCx-aVei7dAReI9946rYmGfePisW__dpY5tFuG-A6v_w0rWcE1xyIcupT1iSFf8tdt9RfOf47ypdp42mrRb9PRasqUMziImpWHR8qbeb-sCOwO8xCwXaHY7fKedEqa2YFbfXAutCTjH67hdI3Vb3dzYzvs2KjX6dnryABE7LMyZ6t978jgg-zyt43tFAAGKykXl45NH0Uz9iOjYB6bsjuXtv3jtwicCSGPna0uLpClWrhOH6MYKKLadHhsRdXvYIJvIK5v-VfHTs99jTmn8NRjZjD-BeJ7Z1nfvZGOeoIad1qCUd6Jdf0Zj57MdmnuwKwfXeFariVPTcaUMt63KlAxFwcgfHUtESRNQg-mXzfHn1gsl1YDdOMdZwzIfiAStZpHWwsLrS4vCt6c2JNxs8ckNyNjQTZ3abZC3BPRpaqLGrEaywS0kzxTO3SS-T_8lypWOnzfmtIYJ0uvLx03cDbQ4BW4-rDM7qw0-RGP-EHNvbE2QbvAT5N4WolRaaqqwG6RpemzVHD_PrWVjl9KgZzmns-tE9TPn3jaB0m0scmSkISlewQDIakgRsaOV-SI8XZ-VCYH8fFApsyv_JGKHMTHSTV3vmTrOx1VHNBYfpYhaTw7d5-PxmtBNi_ycBHqqY1BfD0fcET21y2DdnljOCuHif2lAK3VR8Mity1)



![](https://img.plantuml.biz/plantuml/svg/bLRBRjim4BmRq3yGxg6Fm47Qea2HGn4tGOi02H3Kw5bWg9NCXYO9adBY1ldtBgs7AObIdOljQ6TtPuUpL2wieyQL6q7clszlo1MdXQ4RSWLR44flG3goj9OZ2dyjo59IiSC_oOq7p9DPCdjBLcudW52P4RU63H0Bpd5Ps6Hc7xZKr1TaWbgxTCxm-zB1DLDonVy2EHjWVYZfgeBtIcI3y7VA7WgZIfbTAg4CUPEVvL_pV8XJ9WDJOpwnp_2bqqfZ6Lf059NCwkWHaip9Sp8ZLKk2w1hy4oGOwhYIIwqh224BoXpVGYgeB4eidsvK1g8RuzA1qGRmimxiGUcUjNzgwyS1S10yiI20kLwZT--xqQoY6hPi8Tee1jQcfVNbZTferyRWoHaQv3CitWODI1IqYRMFcG1g42ctI7AlIxf60PNPLP0N_t4GygOcVkjvBpM_5DohtjEn8v_cAItHVj9nLZLuW5qGH5vQuQYJgfvmoHsd0fqv9jwKCg-SilRAzK7__eH3DqmUUy1-wb2Z1mTFm70nss3HEZZA_SweFsWY3DzIYIe5rBUK2telmAjJOnhJijAWGLmGgRjJhSKkUDpIAi2bqOfHLfU1z5VKqHLgx_UuuIPKWGCQB85dqd0AZyi3SYuW5kEPDrVEsxDefjcWgDueF6jyO82Yb18UEsO8beJXlHErK1tgcYyrO3NE37rOw0QysSf1dH2WIjSYUhgjS08ak798ktUU9yzup-5ElP30NVwucZNpuGEn5asph1N6gOWEKoj_LpbLHLX4zYzzv6xTMzCMlyRNae2EvzCCzM2ZJ8PhUGITflwUoc3vUXsM1_dkS6GxB5jVesnDSLaGCfohGIYPywAiDdKQsb24ZAFz0oooUwbUvBz0x0lPDTUuisFli_d7EVcmMEo_HwxgSuBC7ENoo3AHk_2r9SQMFwoJp2ADJa-_HUwpSu8MmvGHO_gaCLP7fCOshacRCk0nRV-NFzKxcGtCUKpBQD9KdsZ2Y5wJELF37eQwm1N0_t7_0G00)




![](https://editor.plantuml.com/uml/bLRTSzCu47_tZF-7dV80F9JZet3N3DCXjC0nGpiTSl2ksXj785j6aXioD_plx4gA8olXohsqqUvlltzQ-PLrmhYXLN3qwV83N4ZH6D721TwYqdsBdOEvjP9GzEkOv4v8XJLyiWZdWlv4YwEoA8lxf5_A3a5KJXjR5lu_URPeZa1O6EZ7AFqWkcOG3SAbhb71_FgznoZLmZqbcvMxKGEEw6rc7x6hqKH_9XwYGMCGkv38OcCTjd2ZXwuMPbCM1YkgeL7u6uKUmRzb0N0VherioHhMsdnTAhtc0g2YiYqyiFXj82ifr4C6auOLvFtyoGpETRUKpM2Gou85EYUxnlgSAwyYSMRrT4OuHLd2j37Uo7gDFsTcpoZOIZXOIxU2UMXXHO8CTZA3TzYX4GuXgJ-ar4GDAJApvpDuyzqPci7OiNDAmbjXKF0vitenYsEQXWdJYgBCv4yALCj3KKXwsEIl6SpxNcr6cskZlr2NfEv2FC7QdJ0pFwL-YrkSfcX9aaGBB5WWpOnPj1j_Fl77C_WiSSrplqLZ1SU3lubDscoyurlIndDkotGno8EvoZnuomxNgIot9jgyrQOb1eYk9cl3HDzluz9Z3ipg2H68UbIXjR1mb4TBJANnsPxQYA4hVT07TMv_miEkjAcdnLy89-BKMSd7t9B8DQ-_3DR53N0jA6Lqv2ACp-kySA_VnB05CRvQmMjqQxhrOyKyXZXB3_3dilWHriBSBnE3oYTfLxAtuUOaa-Kb1SV7wKNTYYRNSCJvsxOzJVYw5UunSQkOq6ACaf9mT37fnbQwHuxHHrfyMV1I7LEDXycjZx9iqhmsuuObPNP_KrLAB-xp-wvIGur_q8uWrBJXPJ5s5XuzEakR2ZDu-L86sxCp0l9cOqoIwoynazn_YThHCOUaCHYPxBSScgg2qwGpTu5tlTf3xhZpFv7_cK36lhiDqeamEEMUnuQnCZGXy1tjJLXzTmRCeIlja5-PNWdPyL9oAuJmwbP4iuxKu7GFUZbzK_yXcDlqiX9gzt3xpvnurnb4EyGlJ4yQh2qvDtfeLgGufVQIXlrp8ZwEuSyB7oa-hVJm7jD3HrNq1Yr_FN1sL3jwztKiAtAAknxfUS3vZNPEj-pzm8j5JoC5Eaq2wPvrmdy86F-zrGPnZ9I5U4K7-huhYvy0)




![](https://img.plantuml.biz/plantuml/svg/lHhDRkCs-XuWxq2aX_5qdC5qjmMsGJke9-Dc3DY9ONlci1U1bcYR3IKA8cLFMiojBr2WsEjU-e3x2FjHf6nI8cLdVdf9BFBxv_TBwISXSI7BbA6BjvCnUatnki0fUassXF4y9Pb40o4eGC6lIrWNT9sXiTg-E3yxFtk2vlA14II8b3HR2xJY1Lh20obGGN22bvHH-N1-9kvfbcD5EsPOY86K1LsMaenYditfhmIzQC7yp3EfgIyvIrhRht1ylovucINNd07NhrOlLlzQhTfml4X8OM3-4V-JVEUmoe4CNfCZKBWe-2wuAq1TmkL3JgvRKk7lapXPALiPJkZYcXS4NVCqvnaOM5oWtyxFa1OMmIcOGxWX6Icmf3mRvBa6GUWIpBKbXQZM8o61qXMGEgoznXBFOHaO6Go6itK9Zr7A4yAYc55WUeN6PdcYLWSvlQxM3KwYHOXe1fhb1O6_LxLpZ0vh1Xh7acv9v3Aw0iyem2LS68UW0w2bg-ofTeNY5zVoM6WX49pdZCRQBc2a5LsNsdesrBC89A0oYdfFpGBZE8bA0NGTfDxJAxJbD35G0eFinw488x5isA6d5QD9hI_WlEAS4PovQ1wRzsozEoWedIXc44PDvgw05fpDnGNA2nuJ8RIwy93cikTu7Jn8ybwv4EI5FhBWB04NPSwC1puhI0pH5J6MHWKHuFM2zEeVDKeVaVSaBYi6YJ5lbC4HWw2kVC2wm9QzOb3K6Bb9zAdhOo181a5UO_Pi2WSvG9LVu3mg_k1e0PrYC7_b3GUxRAYAnmVRd1zKtDUXxO-uVMIR2Ea87gqapYdu0c3I5NrS52bCNCgDmZMHSayUchm02CoKSvf9pzOI2uY4eYcXvgliTKos-engSsatSa3M-ym7RgfSQmr8ek7qJN8uZikqP1XeEYJ3hXjA2U5eqf5A4lUG-gZhOEfT9t6qJgYF5BPr6dgXUH1zrBH_JRxXgbyqdWM8PI0YoIEUamnJOw8mvMuY1T7fctmY7SuOJh4XSbmLE0Umfq5I5cybg2ZUbDbzCvCqk2xf-f5YVqJ-QDVVPku8LzSJ2YZOQajZ4WZ-TfZeV4tsUVWGjP-KM0CrQXzw7Xtxg4kz4qFB7pHEaV6frP2-DaeEcKFko3BI9GSKyDk4P6kQaKYrZW6Aq52dM6g2qATtIk8Sc444k7opfR-UYEXut7H_OXESGHgq76wBASDBHgB3gRhk59S5w2wj_MCEfJgu1ml-qMxaajVaeFE045RQ467JvWK5osFM85v1Hal6u_kz-nI4LMujDZGN-s3sCQFPXXGKPgMOV75UWCjZge7_1iKWdbRuRr1Bq1GA0HJGvCknMXCPUHrOfLwhCr1mbhSbHCG5pIk1Jd529vG2Cze-e1XVGxA1JbdtH4xoTgg40bnHHfem9jmaJGbCwsaEze1gke177vLWasRIRxGZBERGpG4r0N86k9dTQZQX--aH4l6Myb9qJuG1ADCeXO339Su7uYNMpZmx25fIMHQKWWhi58i4JaixbriYD59Luy4IwaXwgLZNfb1vYgpeUyjPDQGzyC2pi1AZI__pJarMMVMwKsC8X61K7GwqDdi0OVozPHnjD9-9J4j03bxPQyPYN105a96T8rSlu7z-4_aSg1xHktjspqs1bqNRfrhqZpOcf_Ao6tL_1tlK1EqkLZUYRQzH9mCfBEDml3nBVAxZCG7DybA6cebkL5vA6rS_VffasirOxIkzEYlPEWVayYQxHYmaIkvKjMag3g9zsFPCHBTc0tLPLES5Y22T6jnCkKy7LUiN7SqLBkUGKW8ALkE248BhX5Y2KlN1kQ9yAwjxMtIjEoVdYd8EP83uND6k-y8VVb2iQFpoPLtHdlscLpuWA_NObtHQDbU5FGvEadrn0HCwgQ7WpEsO8PWDQCjkzOPfXbqimSiYLcF6Yk_3iUvWmpStKpqQy6wbFLDtjADoOoRJUdHqejAs3ir4rKTUXMw4MvU0UzORd2MCEADBf7nOjrB-cp8eLmpQkmrdwe8CKfgw-d-yH2VEhOypOQr8PJvx9lmiqWqEHAPmnA9J97E166_KHAOo1OZmADO-OesBeSz3jJOQIIXqb1z7jjd0Lc-1kWqqc4x7e-l1OdHt6or6Y_6mTZ3qumblc2wwoBqRpkRmtoQuVV7y-nREP3YV3sw6qUnkF8m6y_belXZSBcmq7EJduBwT3sSscWhbRepHxM8ucyw62nVHyjcsXky6Yy7i86SqkdPr_Dz___fF24j9w47uuwyGWYMW1-_FtoyyuK4XMhSmBwXW9LcP6bSvdFxTT7Wx6EdViw4-iA7P6ey7au7-_MfqCxbxFHo7yiC2SdE8nNGCfW7tqKytiy7qpRlHl-tAzGJDxC7l_2pq8ktYcmlqzULbzJzm8tzLrLyCeO9UdaR8SpNtU2AX4T6bv65b4sbVsRZevsU1OlRy-SlWoyShTIbSeNSW-zg20s9N4JYDzJ4AtVnRQVuqfbwqZ-0KiDiHh2wL3wXXxr8q3daxS8e7lm-1Urmk1EepJGYsMsuxyPmakHyX8BkTSso9djIVEDnoII2BPF0FIPuZlWfvYyf24mYlAioWDsN0GYSs2Mq2hCAaGJDSaKC8CuR4Wv0aXPtw2m047HlQyU9-nVZk_0mgE5ACbK2L00LTRwGIeHNTYcJbEg10GbShegvbq9QIdHePr2KuI8yKb6a8z1SQXrisW1MbQiuhTJoybrnAdYhc7PyPQ6a4oc4VIgkIGPZi1OXszwwWpOiECuCZFGAAVcK5fniINRO8Vy3mfcg0XJ9mMcOcgf1g7mysKd3ZyGGwZ950lRkSP8DH7zsC9vVVzg6Kc9THC8_A-FbJLuoVuA5CsVy1)




![](https://img.plantuml.biz/plantuml/svg/hLdRRkCs47qFa7yWt8UwG19ijoXGv66nRf8k32HD43Veey18jCr6fbIIiflz-Wvl4abHijojWNLaQUOCENFcGkrd8J6NpQv4ivU7UtHByORZ7RebUr9MzOumYHP2K922gqkq8dytXEN42SxEpyxFlaSh-LuI98YKb6t4-Pbuewp62aXOXGNdrU6FBStV6142VKp9VE5LK_zQyOBmJlB7OKcSlstWWXKtLLbnzDtwm_gNzJeb_m18U4CM9TqmlQSSlWXFYJw1EsXEQzZlfANuyjCNT4_Ny8yHOyAAVyn_8Zz_61K_Re5Laemkl1CODAj5UgRMQvmNgTNTqZq5k1EsxpHIor1yyfmARCAv187PYo1yXh10ZL2XgpiPD5lKTKbpB6d5dY3GmiZHI6e5pW29bSIIF606WWPGg1kHB6I3vVWNmWZNq615o-EwZgJlCTiqWFTG5QHyubKEbYe3NfQxziQOrgAcDoK5NZejyojIiMjQAlhMdC1tQAqmpuSizjMr5kr-Hme0z1V9rUPzXzNTtKsiSLEnFU52E-mMIxo2u86YTRI-ZZJk_W6x39Ve_lu1BPwMMfJOc-0MMsCiTyxF99LGRVnorOK8_LdnjtLP7OpIab590HbAKmCnK_IiaKSM9q2_wf_dPmW-Yb_eyXFmvnejSkL75N6dOcI0atGFhD4aqqfKgMWcNOC_BIh9FCrCFvt_425Ozgbx-X9TMjljsgmCscDEyMj9X94kI0h3NmuOlqOtd2WHHWveWDIz9Mc2wpjrRRQbunPW3SIvnJAQBOy3tJJn8rMFb85odyDEqTDG005B0uWUgmFJrltFm1dEl5WMVHfu8MXzrWL00Gcr-bigwXA_etoBfLabr5BIWr1S8gmmr0N_hkccuTQQfUxJCduGCzOz9bguwyaZhDKq4QG4bsIb3KssKx6Pw--C5iSOOY3mdcHgBLdkht6O4bwUH7PZUruzLFVRdzh9shZZ5D80VjXwVex0_A07pjKRwgktU-zxpvRVp6FYtBkUuCY0zPv_Q9_kBKPGldk9u9Re9SoeTtfem_vfwW8qZdYepGAjotT6jLgZl4_aeMHum9IXGrlQJJAaEq0_8rRDwuvALGvsjKHSzH6Xaa83s8YDveVVmgyLZheqH3UWsO7AhMMklIEXWLqeHoIOx7Ndhc3uzxrMWeiYsvdnDPELIgoswiwV7-_lifVL1GfiNbrTJMenuQxiYApiGQ6J5V8j7UytyUerunAUclkmQZTcpTu69lSYJdAO7mDmxxhl0Zjw62Ve7rrkgDco8uZ2JR0wW1WgQTFtFBBOuMhtoH-CWDgG8RhEMrP7EC4GvGMhgchq6mGAzhO5LL5NJ13eJWrxCnBguoaxlhXDhYJqqjsWPg8wssOASvy0UaNohi24ZBGg8qPI-VAYIrB0NgIo4-cH4qP1XsUGT8NfF3Eovni8L0b5CGBm-D7pzh0VygDW4GL6Km1aCmSqTnSNi1wIDvfpXIsofoM56iTRxq_BYj587jzqD4F58GvHjvWL9MbRRWxLDoi0NizrTd3fd07pLqwsLGa7Jhyi9-iM199Zhvihw0Xml4eDUS02GmPOQAIWJtD3E9tQSgEwcMZqMIN5fAZX96VJ8DewOqRNwBLdqurT9tw6kuJ3WlgD-DaKgHQOXw83tJS-qdOrriL7Trz_G4gqtVx1k7Dm_EoKzhlyVNh7xUyawBh7ksngePgnnfFE8NEVk1VUEIXZU3TCtU4vr5IIBjSsxRHrcgdUQ6cVbz8xaZcQE8Uep_Z9JXtBthFkvgH51GkBNcYuvy5j7SB0BLqEAgbaLaSHJTY9Eb2qqy1Up7jTb_mVwNDmWB6kr0IUGSepzThtFs4uEcYG0tdD3FqWyUmAIM5TFtDsPYdOU3Xmojf_2Cfxwr2wQrlCs4bbj4i6vp1MDp9QxMdDSQaGJkcAumkg6gbMr5P4U-FRc_YZnZbzg4sMgtOaq-4kmiFJS0CRgQ-3urhN8qHJndFjnEhglw8QFAjEAB9Xontgi-aEa-orhGDx9z2X0_1ZhJO1uojXCFVaHFylXkLlt87lEf5-3rOlFzzRxtRrwFWBej4UmyWXczfdlgd3J30q_ZharEunmM2Yga_h76jQIZ-HqgDM0lxaBk4i3PRu_xqM9rwbMkvEg1l9h8dLqPwImrZQV8Q_q7l-1G00)



![](https://img.plantuml.biz/plantuml/svg/ZLVBRkCs5DqRy3yGxcBQ01vCd-XgC8ha1W8anB3WReek69cIsT2aGD9EaoB_tikNJShAJ1PnoCl3otFVzXUbiTJ70qEBRLsXWk9UuWCgo8amCHm8roXJYW8ALajKuMSY0sendyrd7r2Zdnb1YcXDUQ_cC_L8-O2DbWVSFlPI7Fak5qn8zBIdciI00G2u9xSZt7VTf-xthfj22haZqgD-QdycltwQG3b6ahJ0kcV9YrXAyVJc_LOS1i71w7Smkc2_peaBFM5Wr-5sTmNxkYRADP5mxpt-kc3VvR4_1DSDVI7enz_UEhK-VH1ivwBkCc57Eigffe93u3qQBTQIA70CDd87N22iqBf2_yrdwE8vjCY6WT7M0jTmLLdSjhJh4RJHak03enhEKHxaxaQZj-KOJY1juNa0Dy24e1fpq6eosZ_IwFdirHXpvXsnYMXdrxIXL7mDt15EfBq1bnry6AQfM1gEXLFSDFK8MK6-7k6y5Zl2rbAqS5CuS5MlHs3Fe3IH7YI1p_H6KQx71XRYW6biMt5jMy8X6sZEQF1PLUVVvE2V7k60sJzGZk25s07hUaomv9t4IijZgu-IH4JBQwAvu2SYbNL-WJLkj92WnCBpeZ5eytVMlVeNw77CK4FaYRO-sLQDKvpweAfHjYuT0ZQm3gW4TpyGdfK6Qf7tMJa1sX2NLUICsqpYRcblVMvWwFkxgbx-yeE5tqx2xnd31tnvkmgeL_VlogZGsrUyfznRNwmcxLepQFTc7ZYi2zPsDO6yatZOd-XBZBpxSnKnUVKn3YtZt9cWmCzhAAaIbM7d2xHC075nGkYr5CpLMvxYd0zJNNKAYT9r11ozwLDg16fIq3clJDnIv2fBeHl2eHd3cFJk6i4tgz9v2kpZK2w9hw1xVlpusRa5Fc0OPzLybZcfTG9yWBG0QU6anco_DBVifHAEwx0etQ4no2yjOx-Ew8HuIy9i1DIU3ihmi9qQBPUVVG-E9Qx59XZJyMA1RPR0V1ZirZQviB7zAspipGiiZs6NjItx-GpKNBI3ckjDOIqhIhinRGYMncIRv7vjqzWeo-tM5dVOREBDRRnnTHXFIDLAElWHQQOyahJVQoGw68YcG6vkhkVbpOqvMQAjYYlcKdZA7Hj7Gan2KZ7HqpQvE1mrscE-Ot3i3ZP47Pb69wgEcD4N--Py1YhiDn33FEMOUOvNip5Gp0KqQXoTjWA-Sb3kDHj8cCNA3kB3UH1x8zpKCWOy2VdOCV6aWkgGTqAsUm9puPjq2qytddI1QPXiw61RX75hBoEQeK7Iq1ucpeRp85EH-Gz7PLgg2X5ucr_f-KqDki3J33Cqm6Y3hzs4jyH9apRp9lTBCX3Nvdq4da6LELNYADiq1Z7P3-vn4mF4y0DXoZURl_PqjoFyxsNSQo9XFI4pFQTEHOrlGv78TfacbQrS3Nq1Ql3Jv7y0)


![](https://img.plantuml.biz/plantuml/svg/ZLTDRziu4BqRy7yWqiF6XsAxkrXWuHos-V1s0oI14JS5UcJ4aSGDHMf9oeuB__ZEKA8-BANk8KOilXdEl7ap8tzqdbjV5OgTFTtViHl9CyiBTWDRKAOiG7jswPn45FxtdbqcNcwbtqVWsNmsd_t2DdwlW3dmNkhCiTHOzenVm38BNF1dgT1cFdClKfUS_4S_LpnvoQofjBWs2gtUfH_Ilz9q4cgi0Dl0Va_-W3y_l0txdClaHODpxBSf44PV62t6jwSfJyIFB7ukY07wH2mRAi19ZwisnWcCjMPtcXZ-TjmFniDFa15WKmoG1bffY4P3E-bpvdQoK1opdyyEJmxi0VrHmlFPyZ99Y9I-x5gfNP3FmsLPAfbmBur6k-Mjbbvo9Ry1uzq9GmCFQB2yHh5v88UDlq-WmGOGUc9Ia-iaGEyC5qn0oYlbMM9qAhEgHjOtDw4kDw0WyGmpo2gU0IkC07Kgk2dqaSF8aTJO9AK5_3pbzKsJw7f51u7E21NW4YlBm59fJL4IhyjDzLn8tpqOtVhkJcQvlr8LBAyWaxhrbxLyaZLLBvXZkx_CPumTxcBYzvGuMzSO70a7Ebu-GeBYOHN6szsEpzSMK5z0TTY2TVK5-CN3QuFOW1OuIlwlm7dc3KuQOX744TNiSdqR3EXlbqkSIUSRZweeC0QqTwNH3lvUCEdO-LTm2yA504AWBO8bUQLVBfhJfr84MTtMYiPGgIGjEC0mlkQ-1xE84InNhzxoX0HMb0eBraGvi8oij7TpJ1LU8Qa23GLuAnDtCV0Nwv6WkpPVcRBpBoWLCJZ6MOmTZIdx7FGWwOqto3dKBa6CdO9oNJveS6Uo2AV8KYvLPTlqPLe7Gc9WFEDI1qaWQ_zYHgeLmOrqfU9xTjQfummrBKX-njPvDemFz93ZO31sFrICQ9mHmKRZiYAYI2kr94VAVeEZbeGHJwqq1dYVuvpCygDMhCiGcm5pZrFjDi9Y687EVumjk0_btb98bF6e1eYZ3FRCxRNdhtXWBGJ-7HLS0mWG4RaAgW6KaiOHZKrsliR-y3WHVlraUPblvRT5Wwq_YOx70AR-S5KOo6cb9kI2xfjfsaMvbQwYsHJd9g6EHDCt0rnJ5WNj73PiX4VXTEHrua4AaVx_wdpPFTTeHsyaXoxwtdap7YQAsASn3ewoCqobYWKCoC-MQuUH55Fb6EU7uvSPAt5Eub2OieWfThfinaFJ-JqLqHJ0ZTIqUsoLffwjQ5kjnT6Fs2yITd4-Jo29gvg1Bl79eL2lfnuxVb_2G3H7BHNC7k5z7UHm-NTkeaHZIg1pMiN3GDiRshHYOesZ4Jupk0nk894ExrWRgVtKvAhtsLTGokoM4-XkUDL4uVQIQViUCqNJIk02nQVzDTP4Ks_NTVUSWY6l6xw57_cyCJkjmcj9ByKwaslSXL9NiEY5YtEkd-MeAjsWVJ3rW9dO2sU3TZoIr2DWWmzIZAyEDfo8_b7ldM74m1GlRHRTMw4fwVj7FC6V8zy1)



## 🧱 System Architecture

### 1. LLM Inference Pipeline
- **Data Preparation**: Annotated scenario descriptions + UML mappings
- **Fine-Tuning** (optional): Extend base LLMs (e.g., BART, GPT) for PlantUML generation
- **Inference Equation**:

  \[
  P(t_i \mid t_{<i}) = \text{LLM}(t_1, t_2, \dots, t_{i-1})
  \]

- **API Integration**: FastAPI-based RESTful backend connecting front-end with inference engine

### 2. Frontend Architecture
- Developed using **streamlit**
- Chatbox UI with:
  - Scenario input
  - Diagram rendering panel
  - PlantUML code editor
  - Model configuration sidebar

### 3. Backend Components
- **UMLDiagramGenerationApp**: Coordinates user interactions and rendering pipeline
- **LanguageModelApiClient**: Manages inference calls across different LLM providers
- **DiagramInterpreter**: Converts descriptions into diagrams using PlantUML
- **ProjectionManager**: Filters UML views by inheritance, association, etc.
- **ConversationDataStorage**: Logs and retrieves session data

---

## 🔧 Installation Guide

### 📌 Prerequisites

- Python 3.8+
- `pip` package manager
- Internet access for model inference APIs

### 🛠️ Setup Instructions

```bash
# 1. Clone repository
git clone https://github.com/yourusername/UML-Diagram-Development-Assistant.git
cd UML-Diagram-Development-Assistant

# 2. (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows

# 3. Install core dependencies
pip install streamlit requests

# 4. Optional: Add support for specific LLM APIs
pip install openai replicate llama-cpp-python plantweb

# 5. Run application
streamlit run UML_Diagram_development_Assistant_V1.0.py
````

### 🌐 Access Interface

Open your browser and navigate to:

```
http://localhost:8501
```

---

## 🧭 Application Workflow

### Step 1: Start a Conversation

* Select a language model from the sidebar
* Enter a natural language description (e.g., "A university has students and professors...")

### Step 2: Diagram Generation

* The assistant interprets your input
* PlantUML code is generated and visualized

### Step 3: Iterative Refinement

* Update the scenario or diagram through conversation
* Use projection filters to focus on inheritance, composition, etc.

### Step 4: Editing and Customization

* Modify PlantUML code directly in the editor
* Preview changes in real-time

### Step 5: Session Management

* Your diagrams and conversations are auto-logged
* Resume from previous sessions at any time

---

## 🧩 Technologies Used

| Layer         | Technologies                          |
| ------------- | ------------------------------------- |
| **Frontend**  | ReactJS, Streamlit                    |
| **Backend**   | FastAPI, Python                       |
| **LLMs**      | GPT-4, GLM-4, Replicate, Ollama |
| **Rendering** | PlantUML, Graphviz                    |
| **Packaging** | pip, virtualenv                       |


---

## 🧑‍🤝‍🧑 Contributors

* **Zhentong Ye** ([zye@kean.edu](mailto:zye@kean.edu))
* **Yanwu Lang** ([langy@kean.edu](mailto:langy@kean.edu))

---

## 🔗 Additional Resources

* 📘 [PlantUML Class Diagram Docs](https://plantuml.com/class-diagram)
* 🧭 [UML Class Diagram Tutorial](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)
* 📙 [OOAD Principles Overview](https://www.oodesign.com/)
* 🧪 [BART\_PlantUML Paper](https://arxiv.org/abs/2106.11037)

---

## 📌 Acknowledgements

> *This assistant was built for educational purposes as part of CPS 3962 at Kean University. We gratefully acknowledge the guidance of Dr. Hamza Djigal and the support from the School of Computer Science.*



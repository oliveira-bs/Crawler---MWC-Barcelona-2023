### Crawler - MWC Barcelona 2023

Esse projeto tem como finalidade catalogar as empresas que participaram do [MWC Barcelona 2023](https://www.mwcbarcelona.com/). Para isso, foi desenvolvido um crawler baseado na linguagem python com a ferramenta **Scrapy** .

O objetivo do crawler é obter informações das empresas participantes, aréa de atuação e seus respectivos meios de contato. O processo visou extarir as seguintes informações:

* Nome da empresa (company_name)
* Link Linkedin (linkedIn_url)
* Site da empresa (website)
* Descrição da empresa (company_description)

### Especificações - site

O site da [MWC Barcelona 2023](https://www.mwcbarcelona.com/) é baseado em JavaScript, portanto exige a interação com alguns elementos gráficos da página para realizar ações, por exemplo: carregar próximos produtos por meio do acionamento de um botão.

### Estratégia para raspagem

A estratégia para extrair os dados do site foi acessar o [Sitemaps](https://www.mwcbarcelona.com/sitemaps-1-sitemap.xml) para acessar os setores/seções de exibição do evento. A paginação desses itens foi realizada com a manipulação da url base de cada seção. Os dados extraídos são armazenados em formato *json* no diretório *raw*.


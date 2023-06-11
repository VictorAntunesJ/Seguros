// var myHeaders = new Headers();
// myHeaders.append("Authorization", "Basic dGkzNjA6ZnJvbnQ=");

// var requestOptions = {
//   method: 'GET',
//   headers: myHeaders,
//   redirect: 'follow'
// };

const api =
  'https://api.sheety.co/20e6e67423392ddd3f7dc9eaf5caed47/servicos360Seguros/servicos';

fetch(api)
  .then(resposta => resposta.json())
  .then(dado => {
    var servicosContainer = document.getElementById('home-tab-pane');

    dado.servicos.map(servico => {
      const cartao = document.createElement('div');
      cartao.classList.add('card', 'card-360');

      const corpoDoCartao = document.createElement('div');
      corpoDoCartao.classList.add('card-body');

      const titulo = document.createElement('h5');
      titulo.classList.add('card-title');
      titulo.textContent = servico.nomeDoServico;

      const descricao = document.createElement('p');
      descricao.classList.add('card-text');
      descricao.innerHTML = ` <i class="fa fa-user"></i> ${servico.nomeDoPrestador}`;

      const localizao = document.createElement('p');
      localizao.classList.add('card-text');
      localizao.innerHTML = ` <i class="fa fa-location-dot"></i> ${servico.localizacoDoPrestador}`;

      const seta = document.createElement('i');
      seta.classList.add('fa', 'fa-angle-right', 'seta-360');

      // corpo do cartao
      corpoDoCartao.appendChild(titulo);
      corpoDoCartao.appendChild(descricao);
      corpoDoCartao.appendChild(localizao);
      corpoDoCartao.appendChild(seta);

      // cartao
      cartao.appendChild(corpoDoCartao);

      servicosContainer.appendChild(cartao);
    });
  });

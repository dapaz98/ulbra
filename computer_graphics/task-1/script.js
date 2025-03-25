// Função para inicializar e desenhar em cada contêiner
function createTwoInstance(containerId, params) {
  const elem = document.getElementById(containerId);
  const two = new Two(params).appendTo(elem);
  return two;
}

const lineParams = { width: 500, height: 500 };
const two = createTwoInstance("line-example", lineParams);

// Exemplo 1: Linha
const line = two.makeLine(50, 50, 150, 50);
line.stroke = "blue";
line.linewidth = 3;

two.update();

let direction = 1; // 1 para direita, -1 para esquerda
let speed = 2;

two.bind("update", function () {
  line.translation.x += speed * direction;
  
  if (line.translation.x >= 200) {
    direction = -1; // Inverte a direção
  } else if (line.translation.x <= 0) {
    direction = 1; // Volta a mover para a direita
  }
});

two.play();

// Exemplo 2: Círculo
const circleParams = { width: 500, height: 500 };
const twoCircle = createTwoInstance("circle-example", circleParams);

const circle = twoCircle.makeCircle(250, 250, 100);
circle.fill = "red"; // Cor inicial vermelha
circle.stroke = "black";
circle.linewidth = 2;

twoCircle.update();

let t = 0;
twoCircle.bind("update", function () {
  t += 0.02;
  const r = Math.floor(255 * (Math.sin(t) * 0.5 + 0.5));
  const b = Math.floor(255 * (Math.cos(t) * 0.5 + 0.5));
  circle.fill = `rgb(${r}, 0, ${b})`; // Transição entre vermelho e azul
});

twoCircle.play();

// Exemplo 3: Polígono Regular
const polygonParams = { width: 500, height: 500 };
const twoPolygon = createTwoInstance("polygon-example", polygonParams);

const polygon = twoPolygon.makePolygon(250, 250, 100, 6);
polygon.fill = "red"; 
polygon.stroke = "black"; 
polygon.linewidth = 2;

twoPolygon.update();





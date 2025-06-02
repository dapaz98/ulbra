#include <GL/glut.h>
#include <iostream>

// Variáveis para controle da posição e velocidade
float posX = -0.9f; 
float velocidade = 0.01f; 

// Função de desenho
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();

    // Desenha um quadrado na posição atual
    glPushMatrix();
        glTranslatef(posX, 0.0f, 0.0f);
        glColor3f(0.2f, 0.6f, 0.9f);
        glBegin(GL_QUADS);
            glVertex2f(-0.1f, -0.1f);
            glVertex2f( 0.1f, -0.1f);
            glVertex2f( 0.1f,  0.1f);
            glVertex2f(-0.1f,  0.1f);
        glEnd();
    glPopMatrix();

    glutSwapBuffers();
}

// Função chamada para atualizar a lógica
void update(int value) {
    posX += velocidade;

    // Se passar da borda direita, volta para a esquerda
    if (posX > 1.0f)
        posX = -1.0f;

    glutPostRedisplay();
    glutTimerFunc(16, update, 0); // Aproximadamente 60 FPS
}

// Função para controlar o teclado
void teclado(unsigned char key, int x, int y) {
    if (key == '+') {
        velocidade += 0.005f;
    } else if (key == '-') {
        velocidade -= 0.005f;
        if (velocidade < 0.001f)
            velocidade = 0.001f;
    }
}

// Inicialização do OpenGL
void init() {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Cor de fundo preta
}

// Função principal
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Translacao Simples - OpenGL");

    init();

    glutDisplayFunc(display);
    glutKeyboardFunc(teclado);
    glutTimerFunc(0, update, 0);

    glutMainLoop();
    return 0;
}

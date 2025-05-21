#include <GL/glut.h>
#include <string>

int metodoAtivo = 0;
float rotacaoY = 0.0f;

void displayLegenda() {
    std::string legenda;
    switch (metodoAtivo) {
        case 1: legenda = "Back-Face Culling"; break;
        case 2: legenda = "Z-Buffer"; break;
        case 3: legenda = "Painter's Algorithm"; break;
        default: legenda = "Nenhum metodo ativo";
    }

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();
    gluOrtho2D(-1, 1, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();
    glColor3f(1, 1, 1);
    glRasterPos2f(-0.95f, 0.9f);
    for (char c : legenda)
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, c);
    glPopMatrix();
    glMatrixMode(GL_PROJECTION);
    glPopMatrix();
    glMatrixMode(GL_MODELVIEW);
}

void desenhaCubo(float x, float y, float z, float r, float g, float b) {
    glPushMatrix();
    glTranslatef(x, y, z);
    glColor3f(r, g, b);
    glutSolidCube(1.0);
    glPopMatrix();
}

void desenhaObjetosPadrao() {
    desenhaCubo(-1.5f, 0.0f, -5.0f, 1, 0, 0); // vermelho
    desenhaCubo(0.0f, 0.0f, -6.0f, 0, 1, 0);  // verde
    desenhaCubo(1.5f, 0.0f, -7.0f, 0, 0, 1);  // azul
    desenhaCubo(0.0f, 1.5f, -8.0f, 1, 1, 0);  // amarelo
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    glRotatef(rotacaoY, 0.0f, 1.0f, 0.0f);

    // Reset de estados a cada frame
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_CULL_FACE);

    if (metodoAtivo == 1) {
        glEnable(GL_CULL_FACE);
        glCullFace(GL_BACK);
        desenhaObjetosPadrao();
        glDisable(GL_CULL_FACE);
    }
    else if (metodoAtivo == 2) {
        glEnable(GL_DEPTH_TEST);
        desenhaObjetosPadrao();
        glDisable(GL_DEPTH_TEST);
    }
    else if (metodoAtivo == 3) {
        // Desenho manual do mais distante ao mais próximo
        desenhaCubo(0.0f, 1.5f, -8.0f, 1, 1, 0);  // amarelo
        desenhaCubo(1.5f, 0.0f, -7.0f, 0, 0, 1);  // azul
        desenhaCubo(0.0f, 0.0f, -6.0f, 0, 1, 0);  // verde
        desenhaCubo(-1.5f, 0.0f, -5.0f, 1, 0, 0); // vermelho
    } else {
        desenhaObjetosPadrao();
    }

    displayLegenda();
    glutSwapBuffers();
}

void reshape(int w, int h) {
    if (h == 0) h = 1;
    float aspect = (float)w / h;
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, aspect, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

void teclado(unsigned char key, int x, int y) {
    switch (key) {
        case '1': metodoAtivo = 1; break;
        case '2': metodoAtivo = 2; break;
        case '3': metodoAtivo = 3; break;
        case '0': metodoAtivo = 0; break;
    }
    glutPostRedisplay();
}

void tecladoEspecial(int tecla, int x, int y) {
    if (tecla == GLUT_KEY_LEFT)  rotacaoY -= 5.0f;
    if (tecla == GLUT_KEY_RIGHT) rotacaoY += 5.0f;
    glutPostRedisplay();
}

void inicializa() {
    glEnable(GL_DEPTH_TEST); // Habilita Z-buffer por padrão
    glClearColor(0.1, 0.1, 0.1, 1.0);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Remocao de Partes Ocultas");
    inicializa();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(teclado);
    glutSpecialFunc(tecladoEspecial);
    glutMainLoop();
    return 0;
}

#include <GL/glut.h>
#include <cmath>

bool perspectiva = true;
float anguloSol = 0.0f;
float cameraX = 0, cameraY = 0, cameraZ = 10;

void desenhaCubo() {
    glutSolidCube(1.0);
}

void desenhaArvore() {
    // Tronco
    glPushMatrix();
    glColor3f(0.55f, 0.27f, 0.07f); // marrom
    glTranslatef(0.0f, 0.5f, 0.0f); // sobe meio cubo (altura do tronco)
    glScalef(0.2f, 1.0f, 0.2f);     // tronco estreito e alto
    desenhaCubo();
    glPopMatrix();

    // Copa
    glPushMatrix();
    glColor3f(0.0f, 0.6f, 0.0f); // verde
    glTranslatef(0.0f, 1.3f, 0.0f); // acima do tronco
    glutSolidSphere(0.5, 20, 20);
    glPopMatrix();
}

void desenhaSol() {
    glPushMatrix();
    glColor3f(1.0f, 1.0f, 0.0f); // amarelo
    float raio = 5.0f;
    float x = raio * cos(anguloSol * 3.14 / 180.0f);
    float z = raio * sin(anguloSol * 3.14 / 180.0f);
    glTranslatef(x, 4.0f, z);
    glutSolidSphere(0.4, 20, 20);
    glPopMatrix();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(cameraX, cameraY, cameraZ, 0, 0, 0, 0, 1, 0);

    // chão
    glPushMatrix();
    glColor3f(0.3f, 0.9f, 0.3f); // verde claro
    glTranslatef(0, -1, 0);
    glScalef(20, 0.1, 20);
    desenhaCubo();
    glPopMatrix();

    // árvore 1
    glPushMatrix();
    glTranslatef(-2.0f, 0.0f, -2.0f);
    desenhaArvore();
    glPopMatrix();

    // árvore 2
    glPushMatrix();
    glTranslatef(3.0f, 0.0f, -1.0f);
    desenhaArvore();
    glPopMatrix();

    // sol girando
    desenhaSol();

    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (perspectiva)
        gluPerspective(60.0, (float)w / h, 1.0, 100.0);
    else
        glOrtho(-10, 10, -10, 10, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);
}

void idle() {
    anguloSol += 0.2f;
    if (anguloSol > 360) anguloSol -= 360;
    glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y) {
    if (key == 'p') {
        perspectiva = !perspectiva;
        reshape(600, 600);
    }
}

void specialKeys(int key, int x, int y) {
    if (key == GLUT_KEY_LEFT)  cameraX -= 0.3f;
    if (key == GLUT_KEY_RIGHT) cameraX += 0.3f;
    if (key == GLUT_KEY_UP)    cameraZ -= 0.3f;
    if (key == GLUT_KEY_DOWN)  cameraZ += 0.3f;
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(600, 600);
    glutCreateWindow("Cena 3D com Árvores e Sol Girando");

    glEnable(GL_DEPTH_TEST);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(specialKeys);
    glutIdleFunc(idle);

    glutMainLoop();
    return 0;
}

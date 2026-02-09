// Given a square matrix mat[][], 
// rotate it 90 degrees counterclockwise, 
// modifying the original matrix directly.
// Input: mat[][] = [[1, 2, 3],
//                   [4, 5, 6],
//                   [7, 8, 9]]
// Output: [[3, 6, 9], 
//          [2, 5, 8], 
//          [1, 4, 7]]

#include <stdio.h>
void rotateMatrix(int n, int mat[n][n]) {
    int res[n][n];
    // Rotate the matrix 90 degrees counterclockwise
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            res[n - j - 1][i] = mat[i][j];
        }
    }
    // Copy the rotated matrix back to the original matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            mat[i][j] = res[i][j];
        }
    }
}
int main() {
    int n = 4;
    int mat[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    rotateMatrix(n, mat);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}

// def rotateMatrix(mat):
//     n = len(mat)
    
//     # Reverse each row
//     for row in mat:
//         row.reverse()

//     # Performing Transpose
//     for i in range(n):
//         for j in range(i + 1, n):
//             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


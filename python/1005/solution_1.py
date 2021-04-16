# import java.util.*

stone_numbers = int(input())
stones_weight = [int(x) for x in input().split()]
best = 2000000
# print(best)
for i in range(2 ** (stone_numbers-1)):
    # print(i)
    pile1 = 0
    pile2 = 0
    for j in range(stone_numbers):
        if(((i >> j) & 1) == 1):
            pile1 += stones_weight[j]
        else:
            pile2 += stones_weight[j]
    if (abs(pile1 - pile2) < best):
        best = abs(pile1 - pile2)
print(best)

# public class P5 {
#     public static void main(String[] args) {
#         Scanner in = new Scanner(System.in);
#         int n = in.nextInt();
#         int[] w = new int[n];
#         for(int i=0; i<n; i++)
#             w[i] = in.nextInt();

#         int best = Integer.MAX_VALUE;
#         for(int i=0; i<Math.pow(2,n); i++) {
#             int w1 = 0;
#             int w2 = 0;
#             for(int j=0; j<n; j++) {
#                 if( ((i>>j)&1) == 1)
#                     w1+=w[j];
#                 else w2+=w[j];
#             }
#             if(Math.abs(w1-w2) < best)
#                 best = Math.abs(w1-w2);
#         }
#         System.out.println(best);
#     }
# }

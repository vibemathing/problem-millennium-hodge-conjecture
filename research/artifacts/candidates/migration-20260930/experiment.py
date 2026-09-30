"""Deterministic local candidate checks; no mathematical admission authority."""
import itertools as it, json, sys
from fractions import Fraction

def mul(A,B):
    C={}
    for (a,b),u in A.items():
        for (c,d),v in B.items():
            if a+c<3 and b+d<3: C[a+c,b+d]=C.get((a+c,b+d),0)+u*v
    return {k:v for k,v in C.items() if v}
def hodge_checks():
    # H*(P^2 x P^2,Q)=Q[a,b]/(a^3,b^3), a,b degree 2.
    L={(1,0):1,(0,1):1}; v={(2,0):1,(1,1):-1,(0,2):1}
    assert mul(L,v)=={}
    assert mul(v,v)=={(2,2):3}
    # L: H^2 -> H^4 has columns (1,1,0), (0,1,1).
    # plus primitive v gives determinant 3, hence Q basis, not Z basis.
    M=[[1,0,1],[1,1,-1],[0,1,1]]
    det=M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    assert det==3
    reconstruction_checks=0
    for A,B,C in it.product(range(-4,5),repeat=3):
        z=Fraction(A-B+C,3); x=A-z; y=C-z
        assert (x+z,x+y-z,y+z)==(A,B,C)
        reconstruction_checks+=1
    return {'primitive_vector':[1,-1,1],'L_times_primitive':0,'primitive_self_intersection':3,'decomposition_determinant':det,'integer_test_vectors':reconstruction_checks,'example_a2_decomposition':['2/3','-1/3','1/3']}

if __name__=='__main__':
    print(json.dumps({'python':sys.version.split()[0], 'claim_ceiling':'bounded local regression only', 'hodge':hodge_checks()},indent=2))

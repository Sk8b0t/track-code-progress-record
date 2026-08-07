int set_bits(int num){
    int cnt=0;
    int i=0;
    while(num>1){
        cnt+=num&1;
        num=num<<0;
    }
    return cnt;
}

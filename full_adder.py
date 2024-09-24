class full_adder_sim:
    xor_gate = {"0": {"0": "0", "1": "1"}, "1": {"0": "1", "1": "0"}}
    and_gate = {"0": {"0": "0", "1": "0"}, "1": {"0": "0", "1": "1"}}
    or_gate = {"0": {"0": "0", "1": "1"}, "1": {"0": "1", "1": "1"}}

    half_adder = None
    full_adder = None

    def setup_half_adder(self):
        self.half_adder = {}
        for i in range(0, 2):
            in_1 = str(i)
            self.half_adder[in_1] = {}
            for j in range(0, 2):
                in_2 = str(j)
                sum = self.xor_gate[in_1][in_2]
                carry = self.and_gate[in_1][in_2]
                self.half_adder[in_1][in_2] = [sum, carry]
    
    def setup_full_adder(self):
        self.setup_half_adder()

        self.full_adder = {}

        for i in range(0, 2):
            in_1 = str(i)
            self.full_adder[in_1] = {}
            for j in range(0, 2):
                in_2 = str(j)
                self.full_adder[in_1][in_2] = {}
                for k in range(0, 2):
                    c_in = str(k)
                    sum_carry_1 = self.half_adder[in_1][in_2]
                    sum_carry_2 = self.half_adder[sum_carry_1[0]][c_in]

                    self.full_adder[in_1][in_2][c_in] = [sum_carry_2[0], self.or_gate[sum_carry_1[1]][sum_carry_2[1]]]
        
    def add(self, source_1, source_2):
        result = [""] * (max(len(source_1), len(source_2)) + 1)
        out_1 = len(source_1) - 1
        out_2 = len(source_2) - 1
        in_offset = len(result) - 1
        carry = "0"

        while out_1 > -1 or out_2 > -1:
            in_1 = "0"
            in_2 = "0"
            if out_1 > -1:
                in_1 = source_1[out_1]
            if out_2 > -1:
                in_2 = source_2[out_2]
            sum_carry = self.full_adder[in_1][in_2][carry]

            result[in_offset] = sum_carry[0]
            carry = sum_carry[1]
            out_1 -= 1
            out_2 -= 1
            in_offset -= 1

        if carry == "1":
            result[in_offset] = carry

        bin_string = "".join(result)
        return bin_string
    

    def __init__(self):
        self.setup_full_adder()

def test_full_adder():
    a_full_adder = full_adder_sim()
    #my_full_adder.setup_half_adder()
    #my_half_adder = my_full_adder.half_adder
    #print(f"the half adder is {my_half_adder}\n")
    result = a_full_adder.full_adder
    print(f"the full adder is {result}\n")
#test_full_adder()

def test_add():
    sim = full_adder_sim()
    #a = "11"
    #b = "1"
    #a = "1010"
    #b = "1011"
    a = bin(2 ** 9 - 1)[2:]
    b = "1010101001010011111010010101010010101010"
    result = sim.add(a, b)

    print(f"{a} + {b} = {result}\n")

test_add()
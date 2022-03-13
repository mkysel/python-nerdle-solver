# fill these out
good_letters = []
bad_letters = []
placed_letters = {}


class NerdleSolver:
    # cnt = 0
    all_letters = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    all_operations = {"-", "+", "*", "/"}

    max_length = 8

    def attempt_candidate(self, word):
        # self.cnt += 1
        # if self.cnt % 10000 == 0:
        #     print(f"attempted {self.cnt} words")
        try:
            candidate = eval("".join(word))
            if candidate <= 0:
                # Nerdle does not have negative results
                return None

            if candidate % 1 != 0:
                # integers only
                return None

            return int(candidate)

        except SyntaxError:
            return None

    def validate_candidate(self, word):
        if not set(word).intersection(self.all_operations):
            # there has to be at least 1 operator
            return None

        result = self.attempt_candidate(word)
        if not result:
            return None

        if len(str(result)) + len(word) != self.max_length - 1:
            # wrong length
            return None

        full_word = f"{word}={result}"
        if len(good_letters):
            if not set(full_word).intersection(good_letters):
                return None

        for key, value in placed_letters.items():
            # do some final filtration of both the '=' sign
            # and the result portion
            # the result is never validated before here
            if full_word[key] != value:
                return None

        print(full_word)
        return full_word

    def stage(self, candidate_word):
        index = len(candidate_word)
        if index > self.max_length - 2:
            return

        if index in placed_letters:
            letter = placed_letters[index]
            if letter == "=":
                # all shorter options have already been tried
                return
            word = candidate_word + letter
            self.validate_candidate(word)
            self.stage(word)
        else:
            for letter in self.all_letters:
                if letter in bad_letters:
                    continue
                word = candidate_word + letter
                self.validate_candidate(word)
                self.stage(word)

            if index > 0 and candidate_word[-1] not in self.all_operations:
                for letter in self.all_operations:
                    if letter in bad_letters:
                        continue
                    word = candidate_word + letter
                    self.validate_candidate(word)
                    self.stage(word)

    def solve(self):
        self.stage("")


solver = NerdleSolver()
solver.solve()

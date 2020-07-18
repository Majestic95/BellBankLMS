    def __init__(self, parent, controller, trainees=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        if not trainees:
            self.trainees = []
        else:
            self.trainees = trainees


        trainee1 = tk.Label(self, text="---Add Trainee Here---", bg="lightgrey", fg="blue", pady=10)

        self.trainees.append(trainee1)

        for trainees in self.trainees:
            trainees.pack(side="top", fill="x")

        self.trainee_create = tk.Text(self, font="arial", height=2.5, bg="white",
                                fg="black", borderwidth=2, relief=SUNKEN)

        self.trainee_create.pack(side="bottom", fill="x")
        self.trainee_create.focus_set()

        self.trainee_create.bind("<Return>", self.add_trainee)

        self.color_schemes = [{"bg": "lightgrey", "fg": "blue"}, {"bg": "grey", "fg": "white"}]


    def add_trainee(self, event=None):
        trainee_name = self.trainee_create.get(1.0,END).strip()

        if len(trainee_name) > 0:
            new_trainee = tk.Label(self, text=trainee_name, pady=10)

            _, trainee_style_choice = divmod(len(self.trainees), 2)

            my_scheme_choice = self.color_schemes[trainee_style_choice]

            # new_trainee_configure(bg=my_scheme_choice["bg"])
            # new_trainee_configure(fg=my_scheme_choice["fg"])

            new_trainee.pack(side="top", fill="x")

            self.trainees.append(new_trainee)

        self.trainee_create.delete(1.0, END)
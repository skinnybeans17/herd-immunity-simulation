class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        self.file = f'{self.file_name}'

    def write_metadata(self, virus_name, basic_repro_num, mortality_rate, pop_size, vacc_percentage, initial_infected):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open(self.file_name, 'w+') as f:
            f.write(f"Starting {virus_name} simulation!\n")
            f.write(f"Population size: {pop_size}, percentage vaccinated: {vacc_percentage}%\n")
            f.write(f"Virus mortality rate: {mortality_rate}, reproduction rate: {basic_repro_num}%\n")
            f.write(f"Initially infected people: {initial_infected}")
        f.close()

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        with open(self.file_name, "a+") as f:
            if did_infect:
                f.write(f"{person._id} infected {random_person._id}\n")
            elif random_person_vacc:
                f.write(f"{person._id} didn't infect {random_person._id} because they're already vaccinated.\n")
            elif random_person_sick:
                f.write(f"{person._id} didn't infect {random_person._id} because they've already gotten sick.\n")
            else:
                f.write(f"{person._id} didn't infect {random_person._id}\n")
        f.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        with open(self.file_name, "a+") as f:
            if did_die_from_infection:
                f.write(f"{person._id} died from infection, R.I.P. to them.\n")
            else:
                f.write(f"{person._id} have survived the infection, congrats!\n")
        f.close()

    def log_time_step(self, time_step_number, current_infected, total_dead):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        with open(self.file_name, "a+") as f:
            f.write(f"Time step {time_step_number} has ended. Data will now be analyzed:\n")
            f.write(f"Amount of people infected during time step: {current_infected}\n")
            f.write(f"Amount of people who have died during time step: {total_dead}\n")
        f.close()

    def log_percentage(self, pop_size, total_dead, total_infected, safe_from_vac):
        percentage_infected = f"{float(total_infected / pop_size)}%"
        percentage_dead = f"{float(total_dead / pop_size)}%"

        with open(self.file_name, 'a+') as f:
            f.write(f"Percentage infected: {percentage_infected} percentage that have dead: {percentage_dead} Saved interactions from the vaccination: {safe_from_vac}")

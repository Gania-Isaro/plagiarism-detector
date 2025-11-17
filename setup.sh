#!/bin/bash

# create folders for essays and reports
mkdir -p essays
mkdir -p reports

# log the setup process
echo "Setup started at $(date)" > setup.log
echo "Created directories: essays/ and reports/" >> setup.log
echo "Setup completed successfully at $(date)" >> setup.log

# show message to user
echo "Setup complete. Check (setup.log) for details."


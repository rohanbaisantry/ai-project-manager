### What changes were made?
-

### What was the rationale behind these changes?
-

### Type of Change

- [ ] feat (A new feature)
- [ ] fix (A bugfix)
- [ ] docs (Documentation-only changes)
- [ ] refactor (A code change that neither fixes a bug nor adds a feature)
- [ ] perf (A code change that improves performance)
- [ ] test (Add missing tests or correct existing tests)
- [ ] build (Changes that affect the build system or external dependencies, e.g. gulp, broccoli, npm)
- [ ] ci (Changes to our CI configuration files and scripts, e.g. Travis, Circle, BrowserStack, SauceLabs)
- [ ] chore (Other changes that don't modify src or test files)
- [ ] revert (Reverts a previous commit)
- [ ] style (Changes that do not affect the meaning of the code - whitespace, formatting, etc)

### Where should the reviewer start? :checkered_flag:

### Developer Checklist :heavy_check_mark:

#### Codebase best practices:

- [ ] I did not write a database migration - OR - I've checked that all database migrations are correct and can be
  downgraded without past data loss.
- [ ] I have added relevant data points in the seed data - OR - It is not relevant to my change.
- [ ] I have formatted the code using `black`.
- [ ] I did not change the API contract - OR - I've checked that any changes to the API contract are backward
  compatible, except when deprecating functionality that is no longer in use or will no longer be supported
- [ ] I have added / updated the relevant records in the seed script - OR - it is not needed as the change does not need
  a change in the data.

#### Documentation and Communication:

- [ ] I have reviewed all of my changes, updated required documentation and added comments where needed
- [ ] I have reviewed the ticket to confirm my code meets the acceptance criteria
- [ ] I have included a Screenshot/Video recording video demonstrating functionality in the PR

#### Screenshots/Video of the feature in action: :camera:

- video recording
- Screenshots

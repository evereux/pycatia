# CONTRIBUTING

# Git / Github

If you would like to contribute to pycatia there are a number of ways you can do this.

If your contribution is to the codebase you should learn the basics of git and github and how to create a fork of
pycatia and then a new branch for your specific pull request and creating the pull request itself.

With your pull request please also submit a small section of code that demonstrates how to use the class method you have
added / fixed.

# Which branch should I work on?

The master branch represents the latest released version of pycatia. Any pull requests against the pycatia application
itself shall not be done to this branch but the `developement` branch.

However, changes to the documentation or examples can be done against either.

## Adding new modules

I have now added all the modules I was able to extract from the documentation so there shouldn't be a need to add new
modules as of 0.6.0.

## Examples / User Scripts

New scripts / examples are always welcome as they great for new users to learn how to use pycatia.

Please refer to the existing examples and user_scripts for how to format your code.

If you would like to submit a script / example you can raise an issue or pull request on github. Alternatively you can
email them to me at evereux@gmail.com.

### Examples

Examples should be kept simple and if possible focus on showing how to use a single method.

### User Scripts

These are more advanced scripts that don't fall under the category of examples. Hopefully we can build up a repository
of scripts users will find helpful in their day to day usage of CATIA V5.

## Tests

There is a test framework in place that covers the basic set of pycatia features. However, there is a lot of work to do
here in expanding on those. Pull-requests expanding on these tests would be very much appreciated.


#!/bin/bash -xe
rm -rf exported-artifacts
rm -rf tmp.repos

[[ -d exported-artifacts ]] \
|| mkdir -p exported-artifacts

[[ -d tmp.repos/SOURCES ]] \
|| mkdir -p tmp.repos/SOURCES

spectool --all --get-files --directory tmp.repos/SOURCES wix-toolset-binaries.spec

rpmbuild \
    -D "_topdir $PWD/tmp.repos" \
    -ba wix-toolset-binaries.spec

find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;

rm -rf exported-artifacts
rm -rf tmp.repos

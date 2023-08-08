#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_library.cdk_library_stack import CdkLibraryStack


app = cdk.App()
CdkLibraryStack(app, "cdk-library")

app.synth()

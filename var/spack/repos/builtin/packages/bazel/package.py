# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bazel(Package):
    """Bazel is an open-source build and test tool similar to Make, Maven, and
    Gradle. It uses a human-readable, high-level build language. Bazel supports
    projects in multiple languages and builds outputs for multiple platforms.
    Bazel supports large codebases across multiple repositories, and large
    numbers of users."""

    homepage = "https://bazel.build/"
    url      = "https://github.com/bazelbuild/bazel/releases/download/1.2.0/bazel-1.2.0-dist.zip"

    maintainers = ['adamjstewart']

    version('1.2.1',  sha256='255da49d0f012bc4f2c1d6d3ccdbe578e22fe97b8d124e1629a486fe2a09d3e1')
    version('1.2.0',  sha256='9cb46b0a18b9166730307a0e82bf4c02281a1cc6da0fb11239e6fe4147bdee6e')
    version('1.1.0',  sha256='4b66a8c93af7832ed32e7236cf454a05f3aa06d25a8576fc3f83114f142f95ab')
    version('1.0.1',  sha256='f4d2dfad011ff03a5fae41b9b02cd96cd7297c1205d496603d66516934fbcfee')
    version('1.0.0',  sha256='c61daf0b69dd95205c695b2f9022d296d052c727062cfd396d54ffb2154f8cac')
    version('0.29.1', sha256='872a52cff208676e1169b3e1cae71b1fe572c4109cbd66eab107d8607c378de5')
    version('0.29.0', sha256='01cb6f2e808bd016cf0e217e12373c9efb808123e58b37885be8364458d3a40a')
    version('0.28.1', sha256='2cea463d611f5255d2f3d41c8de5dcc0961adccb39cf0ac036f07070ba720314')
    version('0.28.0', sha256='26ad8cdadd413b8432cf46d9fc3801e8db85d9922f85dd8a7f5a92fec876557f')
    version('0.27.2', sha256='5e1bf2b48e54eb7e518430667d29aef53695d6dd7c718665a52131ab27aadab2')
    version('0.27.1', sha256='8051d77da4ec338acd91770f853e4c25f4407115ed86fd35a6de25921673e779')
    version('0.27.0', sha256='c3080d3b959ac08502ad5c84a51608c291accb1481baad88a628bbf79b30c67a')
    version('0.26.1', sha256='c0e94f8f818759f3f67af798c38683520c540f469cb41aea8f5e5a0e43f11600')
    version('0.26.0', sha256='d26dadf62959255d58e523da3448a6222af768fe1224e321b120c1d5bbe4b4f2')
    version('0.25.3', sha256='23eafd3e439bc71baba9c592b52cb742dabc8640a13b9da1751fec090a2dda99')
    version('0.25.2', sha256='7456032199852c043e6c5b3e4c71dd8089c1158f72ec554e6ec1c77007f0ab51')
    version('0.25.1', sha256='a52bb31aeb1f821e649d25ef48023cfb54a12887aff875c6349ebcac36c2f056')
    version('0.25.0', sha256='f624fe9ca8d51de192655369ac538c420afb7cde16e1ad052554b582fff09287')
    version('0.24.1', sha256='56ea1b199003ad832813621744178e42b39e6206d34fbae342562c287da0cd54')
    version('0.24.0', sha256='621d2a97899a88850a913eabf9285778331a309fd4658b225b1377f80060fa85')
    version('0.23.2', sha256='293a5a7d851e0618eeb5e6958d94a11d45b6a00f2ba9376de61ac2bd5f917439')
    version('0.23.1', sha256='dd47199f92452bf67b2c5d60ad4b7143554eaf2c6196ab6e8713449d81a0491d')
    version('0.23.0', sha256='2daf9c2c6498836ed4ebae7706abb809748b1350cacd35b9f89452f31ac0acc1')
    version('0.22.0', sha256='6860a226c8123770b122189636fb0c156c6e5c9027b5b245ac3b2315b7b55641')
    version('0.21.0', sha256='6ccb831e683179e0cfb351cb11ea297b4db48f9eab987601c038aa0f83037db4')
    version('0.20.0', sha256='1945afa84fd8858b0a3c68c09915a4bc81065c61df2591387b2985e2297d30bd')
    version('0.19.2', sha256='11234cce4f6bdc62c3ac688f41c7b5c178eecb6f7e2c4ba0bcf00ba8565b1d19')
    version('0.19.1', sha256='c9405f7b8c79ebc81f9f0e49bb656df4a0da246771d010c2cdd6bb30e2500ac0')
    version('0.19.0', sha256='ee6135c5c47306c8421d43ad83aabc4f219cb065376ee37797f2c8ba9a615315')
    version('0.18.1', sha256='baed9f28c317000a4ec1ad2571b3939356d22746ca945ac2109148d7abb860d4')
    version('0.18.0', sha256='d0e86d2f7881ec8742a9823a986017452d2da0dfe4e989111da787cb89257155')
    version('0.17.2', sha256='b6e87acfa0a405bb8b3417c58477b66d5bc27dc0d31ba6fa12bc255b9278d33b')
    version('0.17.1', sha256='23e4281c3628cbd746da3f51330109bbf69780bd64461b63b386efae37203f20')
    version('0.16.1', sha256='09c66b94356c82c52f212af52a81ac28eb06de1313755a2f23eeef84d167b36c')
    version('0.16.0', sha256='c730593916ef0ba62f3d113cc3a268e45f7e8039daf7b767c8641b6999bd49b1')
    version('0.15.2', sha256='bf53ec73be3a6d412d85ef612cec6e9c85db45da42001fab0cf1dad44cfc03f1')
    version('0.15.1', sha256='c62b351fa4c1ba5aeb34d0a137176f8e8f1d89a32f548a10e96c11df176ffc6c')
    version('0.15.0', sha256='c3b716e6625e6b8c323350c95cd3ae0f56aeb00458dddd10544d5bead8a7b602')
    version('0.14.1', sha256='d49cdcd82618ae7a7a190e6f0a80d9bf85c1a66b732f994f37732dc14ffb0025')
    version('0.14.0', sha256='259627de8b9d415cc80904523facf3d50e6e8e68448ab968eb1c9cb8ca1ef843')
    version('0.13.1', sha256='b0269e75b40d87ff87886e5f3432cbf88f70c96f907ab588e6c21b2922d72db0')
    version('0.13.0', sha256='82e9035084660b9c683187618a29aa896f8b05b5f16ae4be42a80b5e5b6a7690')
    version('0.12.0', sha256='3b3e7dc76d145046fdc78db7cac9a82bc8939d3b291e53a7ce85315feb827754')
    version('0.11.1', sha256='e8d762bcc01566fa50952c8028e95cfbe7545a39b8ceb3a0d0d6df33b25b333f')
    version('0.11.0', sha256='abfeccc94728cb46be8dbb3507a23ccffbacef9fbda96a977ef4ea8d6ab0d384')
    version('0.10.1', sha256='708248f6d92f2f4d6342006c520f22dffa2f8adb0a9dc06a058e3effe7fee667')
    version('0.10.0', sha256='47e0798caaac4df499bce5fe554a914abd884a855a27085a4473de1d737d9548')
    version('0.9.0',  sha256='efb28fed4ffcfaee653e0657f6500fc4cbac61e32104f4208da385676e76312a')
    version('0.8.1',  sha256='dfd0761e0b7e36c1d74c928ad986500c905be5ebcfbc29914d574af1db7218cf')
    version('0.8.0',  sha256='aa840321d056abd3c6be10c4a1e98a64f9f73fff9aa89c468dae8c003974a078')
    version('0.7.0',  sha256='a084a9c5d843e2343bf3f319154a48abe3d35d52feb0ad45dec427a1c4ffc416')
    version('0.6.1',  sha256='dada1f60a512789747011184b2767d2b44136ef3b036d86947f1896d200d2ba7')
    version('0.6.0',  sha256='a0e53728a9541ef87934831f3d05f2ccfdc3b8aeffe3e037be2b92b12400598e')
    version('0.5.4',  sha256='2157b05309614d6af0e4bbc6065987aede590822634a0522161f3af5d647abc9')
    version('0.5.3',  sha256='76b5c5880a0b15f5b91f7d626c5bc3b76ce7e5d21456963c117ab711bf1c5333')
    version('0.5.2',  sha256='2418c619bdd44257a170b85b9d2ecb75def29e751b725e27186468ada2e009ea')
    version('0.5.1',  sha256='85e6a18b111afeea2e475fe991db2a441ec3824211d659bee7b0012c36be9a40')
    version('0.5.0',  sha256='ebba7330a8715e96a6d6dc0aa085125d529d0740d788f0544c6169d892e4f861')
    version('0.4.5',  sha256='2b737be42678900470ae9e48c975ac5b2296d9ae23c007bf118350dbe7c0552b')
    version('0.4.4',  sha256='d52a21dda271ae645711ce99c70cf44c5d3a809138e656bbff00998827548ebb')
    version('0.4.3',  sha256='cbd2ab580181c17317cf18b2bf825bcded2d97cab01cd5b5fe4f4d520b64f90f')
    version('0.4.2',  sha256='8e6f41252abadcdb2cc7a07f910ec4b45fb12c46f0a578672c6a186c7efcdb36')
    version('0.4.1',  sha256='008c648d3c46ece063ae8b5008480d8ae6d359d35967356685d1c09da07e1064')
    version('0.4.0',  sha256='6474714eee72ba2d4e271ed00ce8c05d67a9d15327bc03962b821b2af2c5ca36')
    version('0.3.2',  sha256='ca5caf7b2b48c7639f45d815b32e76d69650f3199eb8caa541d402722e3f6c10')
    version('0.3.1',  sha256='218d0e28b4d1ee34585f2ac6b18d169c81404d93958815e73e60cc0368efcbb7')
    version('0.3.0',  sha256='357fd8bdf86034b93902616f0844bd52e9304cccca22971ab7007588bf9d5fb3')

    # https://docs.bazel.build/versions/master/install-compile-source.html#bootstrap-bazel
    # Until https://github.com/spack/spack/issues/14058 is fixed, use jdk to build bazel
    # Strict dependency on java@8 as per
    # https://docs.bazel.build/versions/master/install-compile-source.html#bootstrap-unix-prereq
    depends_on('jdk@1.8.0:1.8.999', type=('build', 'run'))
    depends_on('python', type=('build', 'run'))

    # Pass Spack environment variables to the build
    patch('bazelruleclassprovider-0.25.patch', when='@0.25:')
    patch('bazelruleclassprovider-0.14.patch', when='@0.14:0.24')
    patch('bazelconfiguration-0.3.patch', when='@:0.13')

    # Inject include paths
    patch('unix_cc_configure-0.15.patch',  when='@0.15:')
    patch('unix_cc_configure-0.10.patch',  when='@0.10:0.14')
    patch('unix_cc_configure-0.5.3.patch', when='@0.5.3:0.9')
    patch('cc_configure-0.5.0.patch', when='@0.5.0:0.5.2')
    patch('cc_configure-0.3.0.patch', when='@:0.4')

    # Set CC and CXX
    patch('compile-0.29.patch', when='@0.29:')
    patch('compile-0.21.patch', when='@0.21:0.28')
    patch('compile-0.16.patch', when='@0.16:0.20')
    patch('compile-0.13.patch', when='@0.13:0.15')
    patch('compile-0.9.patch',  when='@0.9:0.12')
    patch('compile-0.6.patch',  when='@0.6:0.8')
    patch('compile-0.4.patch',  when='@0.4:0.5')
    patch('compile-0.3.patch',  when='@:0.3')

    phases = ['bootstrap', 'install']

    def url_for_version(self, version):
        if version >= Version('0.4.1'):
            url = 'https://github.com/bazelbuild/bazel/releases/download/{0}/bazel-{0}-dist.zip'
        else:
            url = 'https://github.com/bazelbuild/bazel/archive/{0}.tar.gz'

        return url.format(version)

    def setup_build_environment(self, env):
        env.set('EXTRA_BAZEL_ARGS',
                # Spack's logs don't handle colored output well
                '--color=no --host_javabase=@local_jdk//:jdk')

    def bootstrap(self, spec, prefix):
        bash = which('bash')
        bash('./compile.sh')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('output/bazel', prefix.bin)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def test(self):
        # https://github.com/Homebrew/homebrew-core/blob/master/Formula/bazel.rb

        # Bazel does not work properly on NFS, switch to /tmp
        with working_dir('/tmp/spack/bazel/spack-test', create=True):
            touch('WORKSPACE')

            with open('ProjectRunner.java', 'w') as f:
                f.write("""\
public class ProjectRunner {
    public static void main(String args[]) {
        System.out.println("Hi!");
    }
}""")

            with open('BUILD', 'w') as f:
                f.write("""\
java_binary(
    name = "bazel-test",
    srcs = glob(["*.java"]),
    main_class = "ProjectRunner",
)""")

            # Spack's logs don't handle colored output well
            bazel = Executable(self.prefix.bin.bazel)
            bazel('--output_user_root=/tmp/spack/bazel/spack-test',
                  'build', '--color=no', '//:bazel-test')

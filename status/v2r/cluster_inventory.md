# V2R cluster inventory

2026-09-27T10:04:55.997343+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314437312512 available bytes; 82.46% used; 112440710 free inodes.

server1 `/home`: 314437312512 available bytes; 82.46% used; 112440710 free inodes.

server1 `/tmp`: 314437312512 available bytes; 82.46% used; 112440710 free inodes.

server1 `/var/tmp`: 314437312512 available bytes; 82.46% used; 112440710 free inodes.

server1 `/mnt/raid5`: 635425009664 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16506531840 available bytes; 99.08% used; 110356831 free inodes.

server2 `/home`: 16506531840 available bytes; 99.08% used; 110356831 free inodes.

server2 `/tmp`: 16506531840 available bytes; 99.08% used; 110356831 free inodes.

server2 `/var/tmp`: 16506531840 available bytes; 99.08% used; 110356831 free inodes.

server2 `/mnt/raid5`: 572569227264 available bytes; 96.04% used; 444740283 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78545285120 available bytes; 95.62% used; 114062834 free inodes.

server3 `/home`: 78545285120 available bytes; 95.62% used; 114062834 free inodes.

server3 `/data`: 1332247748608 available bytes; 81.59% used; 225761472 free inodes.

server3 `/tmp`: 78545285120 available bytes; 95.62% used; 114062834 free inodes.

server3 `/var/tmp`: 78545285120 available bytes; 95.62% used; 114062834 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111049445376 available bytes; 93.80% used; 114372847 free inodes.

server4 `/home`: 111049445376 available bytes; 93.80% used; 114372847 free inodes.

server4 `/data`: 363945652224 available bytes; 94.97% used; 224767054 free inodes.

server4 `/tmp`: 111049445376 available bytes; 93.80% used; 114372847 free inodes.

server4 `/var/tmp`: 111049445376 available bytes; 93.80% used; 114372847 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

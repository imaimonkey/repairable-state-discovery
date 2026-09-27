# V2R cluster inventory

2026-09-27T11:02:51.503539+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 312321323008 available bytes; 82.58% used; 112435599 free inodes.

server1 `/home`: 312321323008 available bytes; 82.58% used; 112435599 free inodes.

server1 `/tmp`: 312321323008 available bytes; 82.58% used; 112435599 free inodes.

server1 `/var/tmp`: 312321323008 available bytes; 82.58% used; 112435599 free inodes.

server1 `/mnt/raid5`: 635400663040 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16437305344 available bytes; 99.08% used; 110353761 free inodes.

server2 `/home`: 16437305344 available bytes; 99.08% used; 110353761 free inodes.

server2 `/tmp`: 16437305344 available bytes; 99.08% used; 110353761 free inodes.

server2 `/var/tmp`: 16437305344 available bytes; 99.08% used; 110353761 free inodes.

server2 `/mnt/raid5`: 570323800064 available bytes; 96.06% used; 444737862 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543208448 available bytes; 95.62% used; 114062816 free inodes.

server3 `/home`: 78543208448 available bytes; 95.62% used; 114062816 free inodes.

server3 `/data`: 1332017438720 available bytes; 81.59% used; 225760293 free inodes.

server3 `/tmp`: 78543208448 available bytes; 95.62% used; 114062816 free inodes.

server3 `/var/tmp`: 78543208448 available bytes; 95.62% used; 114062816 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030968320 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111030968320 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 362866356224 available bytes; 94.99% used; 224764629 free inodes.

server4 `/tmp`: 111030968320 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111030968320 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

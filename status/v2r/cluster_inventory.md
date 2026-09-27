# V2R cluster inventory

2026-09-27T09:26:51.370844+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314452307968 available bytes; 82.46% used; 112440737 free inodes.

server1 `/home`: 314452307968 available bytes; 82.46% used; 112440737 free inodes.

server1 `/tmp`: 314452307968 available bytes; 82.46% used; 112440737 free inodes.

server1 `/var/tmp`: 314452307968 available bytes; 82.46% used; 112440737 free inodes.

server1 `/mnt/raid5`: 635456516096 available bytes; 97.08% used; 337424509 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16509251584 available bytes; 99.08% used; 110356964 free inodes.

server2 `/home`: 16509251584 available bytes; 99.08% used; 110356964 free inodes.

server2 `/tmp`: 16509251584 available bytes; 99.08% used; 110356964 free inodes.

server2 `/var/tmp`: 16509251584 available bytes; 99.08% used; 110356964 free inodes.

server2 `/mnt/raid5`: 573746794496 available bytes; 96.04% used; 444741934 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78554832896 available bytes; 95.62% used; 114062914 free inodes.

server3 `/home`: 78554832896 available bytes; 95.62% used; 114062914 free inodes.

server3 `/data`: 1332498378752 available bytes; 81.58% used; 225762450 free inodes.

server3 `/tmp`: 78554832896 available bytes; 95.62% used; 114062914 free inodes.

server3 `/var/tmp`: 78554832896 available bytes; 95.62% used; 114062914 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050469376 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111050469376 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364009623552 available bytes; 94.97% used; 224767342 free inodes.

server4 `/tmp`: 111050469376 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111050469376 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

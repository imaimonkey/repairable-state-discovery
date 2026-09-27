# V2R cluster inventory

2026-09-27T14:21:06.750168+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304744083456 available bytes; 83.00% used; 112401355 free inodes.

server1 `/home`: 304744083456 available bytes; 83.00% used; 112401355 free inodes.

server1 `/tmp`: 304744083456 available bytes; 83.00% used; 112401355 free inodes.

server1 `/var/tmp`: 304744083456 available bytes; 83.00% used; 112401355 free inodes.

server1 `/mnt/raid5`: 630252773376 available bytes; 97.11% used; 337424060 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13415555072 available bytes; 99.25% used; 110351810 free inodes.

server2 `/home`: 13415555072 available bytes; 99.25% used; 110351810 free inodes.

server2 `/tmp`: 13415555072 available bytes; 99.25% used; 110351810 free inodes.

server2 `/var/tmp`: 13415555072 available bytes; 99.25% used; 110351810 free inodes.

server2 `/mnt/raid5`: 527077056512 available bytes; 96.36% used; 444722705 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78558212096 available bytes; 95.62% used; 114062769 free inodes.

server3 `/home`: 78558212096 available bytes; 95.62% used; 114062769 free inodes.

server3 `/data`: 1328731398144 available bytes; 81.64% used; 225756965 free inodes.

server3 `/tmp`: 78558212096 available bytes; 95.62% used; 114062769 free inodes.

server3 `/var/tmp`: 78558212096 available bytes; 95.62% used; 114062769 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110992478208 available bytes; 93.81% used; 114372781 free inodes.

server4 `/home`: 110992478208 available bytes; 93.81% used; 114372781 free inodes.

server4 `/data`: 350540201984 available bytes; 95.16% used; 224727382 free inodes.

server4 `/tmp`: 110992478208 available bytes; 93.81% used; 114372781 free inodes.

server4 `/var/tmp`: 110992478208 available bytes; 93.81% used; 114372781 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

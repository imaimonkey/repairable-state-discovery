# V2R cluster inventory

2026-09-27T14:22:38.376914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304737230848 available bytes; 83.00% used; 112401357 free inodes.

server1 `/home`: 304737230848 available bytes; 83.00% used; 112401357 free inodes.

server1 `/tmp`: 304737230848 available bytes; 83.00% used; 112401357 free inodes.

server1 `/var/tmp`: 304737230848 available bytes; 83.00% used; 112401357 free inodes.

server1 `/mnt/raid5`: 630251331584 available bytes; 97.11% used; 337424058 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13415108608 available bytes; 99.25% used; 110351809 free inodes.

server2 `/home`: 13415108608 available bytes; 99.25% used; 110351809 free inodes.

server2 `/tmp`: 13415108608 available bytes; 99.25% used; 110351809 free inodes.

server2 `/var/tmp`: 13415108608 available bytes; 99.25% used; 110351809 free inodes.

server2 `/mnt/raid5`: 526489444352 available bytes; 96.36% used; 444722547 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78559035392 available bytes; 95.62% used; 114062759 free inodes.

server3 `/home`: 78559035392 available bytes; 95.62% used; 114062759 free inodes.

server3 `/data`: 1328729587712 available bytes; 81.64% used; 225756914 free inodes.

server3 `/tmp`: 78559035392 available bytes; 95.62% used; 114062759 free inodes.

server3 `/var/tmp`: 78559035392 available bytes; 95.62% used; 114062759 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110992441344 available bytes; 93.81% used; 114372781 free inodes.

server4 `/home`: 110992441344 available bytes; 93.81% used; 114372781 free inodes.

server4 `/data`: 350540050432 available bytes; 95.16% used; 224727382 free inodes.

server4 `/tmp`: 110992441344 available bytes; 93.81% used; 114372781 free inodes.

server4 `/var/tmp`: 110992441344 available bytes; 93.81% used; 114372781 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

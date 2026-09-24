# V2R cluster inventory

2026-09-24T18:46:14.107216+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004134912 available bytes; 81.92% used; 112481456 free inodes.

server1 `/home`: 324004134912 available bytes; 81.92% used; 112481456 free inodes.

server1 `/tmp`: 324004134912 available bytes; 81.92% used; 112481456 free inodes.

server1 `/var/tmp`: 324004134912 available bytes; 81.92% used; 112481456 free inodes.

server1 `/mnt/raid5`: 395639422976 available bytes; 98.19% used; 337637520 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54479081472 available bytes; 96.96% used; 110411940 free inodes.

server2 `/home`: 54479081472 available bytes; 96.96% used; 110411940 free inodes.

server2 `/tmp`: 54479081472 available bytes; 96.96% used; 110411940 free inodes.

server2 `/var/tmp`: 54479081472 available bytes; 96.96% used; 110411940 free inodes.

server2 `/mnt/raid5`: 496229277696 available bytes; 96.57% used; 445160157 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84407906304 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84407906304 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152740589568 available bytes; 97.89% used; 225800246 free inodes.

server3 `/tmp`: 84407906304 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84407906304 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661607936 available bytes; 94.10% used; 114348497 free inodes.

server4 `/home`: 105661607936 available bytes; 94.10% used; 114348497 free inodes.

server4 `/data`: 90023063552 available bytes; 98.76% used; 225267745 free inodes.

server4 `/tmp`: 105661607936 available bytes; 94.10% used; 114348497 free inodes.

server4 `/var/tmp`: 105661607936 available bytes; 94.10% used; 114348497 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

# V2R cluster inventory

2026-09-24T07:06:16.037223+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324479574016 available bytes; 81.90% used; 112491324 free inodes.

server1 `/home`: 324479574016 available bytes; 81.90% used; 112491324 free inodes.

server1 `/tmp`: 324479574016 available bytes; 81.90% used; 112491324 free inodes.

server1 `/var/tmp`: 324479574016 available bytes; 81.90% used; 112491324 free inodes.

server1 `/mnt/raid5`: 517434376192 available bytes; 97.63% used; 337722839 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57860571136 available bytes; 96.77% used; 110431167 free inodes.

server2 `/home`: 57860571136 available bytes; 96.77% used; 110431167 free inodes.

server2 `/tmp`: 57860571136 available bytes; 96.77% used; 110431167 free inodes.

server2 `/var/tmp`: 57860571136 available bytes; 96.77% used; 110431167 free inodes.

server2 `/mnt/raid5`: 518577967104 available bytes; 96.42% used; 445190677 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127167930368 available bytes; 92.90% used; 114199243 free inodes.

server3 `/home`: 127167930368 available bytes; 92.90% used; 114199243 free inodes.

server3 `/data`: 139152814080 available bytes; 98.08% used; 225834650 free inodes.

server3 `/tmp`: 127167930368 available bytes; 92.90% used; 114199243 free inodes.

server3 `/var/tmp`: 127167930368 available bytes; 92.90% used; 114199243 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790210048 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790210048 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 299502010368 available bytes; 95.86% used; 225367555 free inodes.

server4 `/tmp`: 105790210048 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790210048 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

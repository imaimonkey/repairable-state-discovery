# V2R cluster inventory

2026-09-24T00:21:10.639450+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325555802112 available bytes; 81.84% used; 112500684 free inodes.

server1 `/home`: 325555802112 available bytes; 81.84% used; 112500684 free inodes.

server1 `/tmp`: 325555802112 available bytes; 81.84% used; 112500684 free inodes.

server1 `/var/tmp`: 325555802112 available bytes; 81.84% used; 112500684 free inodes.

server1 `/mnt/raid5`: 1178812690432 available bytes; 94.59% used; 337735241 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41006559232 available bytes; 97.71% used; 110432371 free inodes.

server2 `/home`: 41006559232 available bytes; 97.71% used; 110432371 free inodes.

server2 `/tmp`: 41006559232 available bytes; 97.71% used; 110432371 free inodes.

server2 `/var/tmp`: 41006559232 available bytes; 97.71% used; 110432371 free inodes.

server2 `/mnt/raid5`: 533074083840 available bytes; 96.32% used; 445203839 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292637687808 available bytes; 83.67% used; 114209079 free inodes.

server3 `/home`: 292637687808 available bytes; 83.67% used; 114209079 free inodes.

server3 `/data`: 82246635520 available bytes; 98.86% used; 225844384 free inodes.

server3 `/tmp`: 292637687808 available bytes; 83.67% used; 114209079 free inodes.

server3 `/var/tmp`: 292637687808 available bytes; 83.67% used; 114209079 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094919680 available bytes; 94.08% used; 114350579 free inodes.

server4 `/home`: 106094919680 available bytes; 94.08% used; 114350579 free inodes.

server4 `/data`: 292915236864 available bytes; 95.95% used; 225414567 free inodes.

server4 `/tmp`: 106094919680 available bytes; 94.08% used; 114350579 free inodes.

server4 `/var/tmp`: 106094919680 available bytes; 94.08% used; 114350579 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

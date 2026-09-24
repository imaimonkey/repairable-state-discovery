# V2R cluster inventory

2026-09-24T15:16:58.963162+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045168640 available bytes; 81.92% used; 112481455 free inodes.

server1 `/home`: 324045168640 available bytes; 81.92% used; 112481455 free inodes.

server1 `/tmp`: 324045168640 available bytes; 81.92% used; 112481455 free inodes.

server1 `/var/tmp`: 324045168640 available bytes; 81.92% used; 112481455 free inodes.

server1 `/mnt/raid5`: 416793255936 available bytes; 98.09% used; 337662739 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57405534208 available bytes; 96.80% used; 110427639 free inodes.

server2 `/home`: 57405534208 available bytes; 96.80% used; 110427639 free inodes.

server2 `/tmp`: 57405534208 available bytes; 96.80% used; 110427639 free inodes.

server2 `/var/tmp`: 57405534208 available bytes; 96.80% used; 110427639 free inodes.

server2 `/mnt/raid5`: 502592618496 available bytes; 96.53% used; 445166441 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84614860800 available bytes; 95.28% used; 114172743 free inodes.

server3 `/home`: 84614860800 available bytes; 95.28% used; 114172743 free inodes.

server3 `/data`: 160470618112 available bytes; 97.78% used; 225807204 free inodes.

server3 `/tmp`: 84614860800 available bytes; 95.28% used; 114172743 free inodes.

server3 `/var/tmp`: 84614860800 available bytes; 95.28% used; 114172743 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716809728 available bytes; 94.10% used; 114348633 free inodes.

server4 `/home`: 105716809728 available bytes; 94.10% used; 114348633 free inodes.

server4 `/data`: 68782407680 available bytes; 99.05% used; 225256957 free inodes.

server4 `/tmp`: 105716809728 available bytes; 94.10% used; 114348633 free inodes.

server4 `/var/tmp`: 105716809728 available bytes; 94.10% used; 114348633 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

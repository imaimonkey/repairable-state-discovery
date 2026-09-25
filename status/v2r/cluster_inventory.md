# V2R cluster inventory

2026-09-25T03:15:59.110032+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318939828224 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318939828224 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318939828224 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318939828224 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 416115429376 available bytes; 98.09% used; 337600580 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22990548992 available bytes; 98.72% used; 110410458 free inodes.

server2 `/home`: 22990548992 available bytes; 98.72% used; 110410458 free inodes.

server2 `/tmp`: 22990548992 available bytes; 98.72% used; 110410458 free inodes.

server2 `/var/tmp`: 22990548992 available bytes; 98.72% used; 110410458 free inodes.

server2 `/mnt/raid5`: 465614311424 available bytes; 96.78% used; 445112315 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84343353344 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84343353344 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144771821568 available bytes; 98.00% used; 225810184 free inodes.

server3 `/tmp`: 84343353344 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84343353344 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692737536 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692737536 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 47029501952 available bytes; 99.35% used; 224967089 free inodes.

server4 `/tmp`: 105692737536 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692737536 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

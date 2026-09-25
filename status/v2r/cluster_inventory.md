# V2R cluster inventory

2026-09-25T21:44:55.151508+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318699692032 available bytes; 82.22% used; 112476300 free inodes.

server1 `/home`: 318699692032 available bytes; 82.22% used; 112476300 free inodes.

server1 `/tmp`: 318699692032 available bytes; 82.22% used; 112476300 free inodes.

server1 `/var/tmp`: 318699692032 available bytes; 82.22% used; 112476300 free inodes.

server1 `/mnt/raid5`: 360330600448 available bytes; 98.35% used; 337539182 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22899462144 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22899462144 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22899462144 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22899462144 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 300818223104 available bytes; 97.92% used; 445054062 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84222595072 available bytes; 95.30% used; 114152625 free inodes.

server3 `/home`: 84222595072 available bytes; 95.30% used; 114152625 free inodes.

server3 `/data`: 125889556480 available bytes; 98.26% used; 225806746 free inodes.

server3 `/tmp`: 84222595072 available bytes; 95.30% used; 114152625 free inodes.

server3 `/var/tmp`: 84222595072 available bytes; 95.30% used; 114152625 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105388556288 available bytes; 94.12% used; 114347330 free inodes.

server4 `/home`: 105388556288 available bytes; 94.12% used; 114347330 free inodes.

server4 `/data`: 215897165824 available bytes; 97.02% used; 224919372 free inodes.

server4 `/tmp`: 105388556288 available bytes; 94.12% used; 114347330 free inodes.

server4 `/var/tmp`: 105388556288 available bytes; 94.12% used; 114347330 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

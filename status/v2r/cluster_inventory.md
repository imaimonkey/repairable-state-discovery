# V2R cluster inventory

2026-09-25T21:34:13.169449+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318702149632 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318702149632 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318702149632 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318702149632 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 360519610368 available bytes; 98.35% used; 337539263 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22905335808 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905335808 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905335808 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905335808 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301133467648 available bytes; 97.92% used; 445054637 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84367814656 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84367814656 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 125893910528 available bytes; 98.26% used; 225806916 free inodes.

server3 `/tmp`: 84367814656 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84367814656 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105388920832 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105388920832 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 216842268672 available bytes; 97.00% used; 224919919 free inodes.

server4 `/tmp`: 105388920832 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105388920832 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

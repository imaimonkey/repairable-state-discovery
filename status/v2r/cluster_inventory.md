# V2R cluster inventory

2026-09-26T03:48:11.054323+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416556032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318416556032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318416556032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318416556032 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330983845888 available bytes; 98.48% used; 337545722 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940725248 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22940725248 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22940725248 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22940725248 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 286704500736 available bytes; 98.02% used; 445051764 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309385216 available bytes; 95.30% used; 114152348 free inodes.

server3 `/home`: 84309385216 available bytes; 95.30% used; 114152348 free inodes.

server3 `/data`: 125356486656 available bytes; 98.27% used; 225830282 free inodes.

server3 `/tmp`: 84309385216 available bytes; 95.30% used; 114152348 free inodes.

server3 `/var/tmp`: 84309385216 available bytes; 95.30% used; 114152348 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105766133760 available bytes; 94.10% used; 114346781 free inodes.

server4 `/home`: 105766133760 available bytes; 94.10% used; 114346781 free inodes.

server4 `/data`: 108816363520 available bytes; 98.50% used; 224914679 free inodes.

server4 `/tmp`: 105766133760 available bytes; 94.10% used; 114346781 free inodes.

server4 `/var/tmp`: 105766133760 available bytes; 94.10% used; 114346781 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

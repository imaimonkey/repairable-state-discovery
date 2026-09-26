# V2R cluster inventory

2026-09-26T03:40:33.250846+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417063936 available bytes; 82.24% used; 112476270 free inodes.

server1 `/home`: 318417063936 available bytes; 82.24% used; 112476270 free inodes.

server1 `/tmp`: 318417063936 available bytes; 82.24% used; 112476270 free inodes.

server1 `/var/tmp`: 318417063936 available bytes; 82.24% used; 112476270 free inodes.

server1 `/mnt/raid5`: 330994786304 available bytes; 98.48% used; 337545751 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939504640 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22939504640 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22939504640 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22939504640 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 286385647616 available bytes; 98.02% used; 445052009 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309368832 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84309368832 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125361229824 available bytes; 98.27% used; 225830404 free inodes.

server3 `/tmp`: 84309368832 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84309368832 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105766359040 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766359040 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108869644288 available bytes; 98.50% used; 224914717 free inodes.

server4 `/tmp`: 105766359040 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766359040 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

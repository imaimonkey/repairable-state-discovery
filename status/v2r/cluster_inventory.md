# V2R cluster inventory

2026-09-26T03:55:48.922110+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318415060992 available bytes; 82.24% used; 112476261 free inodes.

server1 `/home`: 318415060992 available bytes; 82.24% used; 112476261 free inodes.

server1 `/tmp`: 318415060992 available bytes; 82.24% used; 112476261 free inodes.

server1 `/var/tmp`: 318415060992 available bytes; 82.24% used; 112476261 free inodes.

server1 `/mnt/raid5`: 330965753856 available bytes; 98.48% used; 337545691 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931865600 available bytes; 98.72% used; 110406194 free inodes.

server2 `/home`: 22931865600 available bytes; 98.72% used; 110406194 free inodes.

server2 `/tmp`: 22931865600 available bytes; 98.72% used; 110406194 free inodes.

server2 `/var/tmp`: 22931865600 available bytes; 98.72% used; 110406194 free inodes.

server2 `/mnt/raid5`: 286495289344 available bytes; 98.02% used; 445051483 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84677308416 available bytes; 95.27% used; 114177490 free inodes.

server3 `/home`: 84677308416 available bytes; 95.27% used; 114177490 free inodes.

server3 `/data`: 124606849024 available bytes; 98.28% used; 225820489 free inodes.

server3 `/tmp`: 84677308416 available bytes; 95.27% used; 114177490 free inodes.

server3 `/var/tmp`: 84677308416 available bytes; 95.27% used; 114177490 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105698742272 available bytes; 94.10% used; 114346606 free inodes.

server4 `/home`: 105698742272 available bytes; 94.10% used; 114346606 free inodes.

server4 `/data`: 109779267584 available bytes; 98.48% used; 224929549 free inodes.

server4 `/tmp`: 105698742272 available bytes; 94.10% used; 114346606 free inodes.

server4 `/var/tmp`: 105698742272 available bytes; 94.10% used; 114346606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

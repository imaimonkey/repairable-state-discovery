# V2R cluster inventory

2026-09-25T07:34:40.656169+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318870855680 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318870855680 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318870855680 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318870855680 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 385876090880 available bytes; 98.23% used; 337558399 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22859816960 available bytes; 98.72% used; 110410514 free inodes.

server2 `/home`: 22859816960 available bytes; 98.72% used; 110410514 free inodes.

server2 `/tmp`: 22859816960 available bytes; 98.72% used; 110410514 free inodes.

server2 `/var/tmp`: 22859816960 available bytes; 98.72% used; 110410514 free inodes.

server2 `/mnt/raid5`: 342293155840 available bytes; 97.63% used; 445096904 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84437475328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84437475328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142397419520 available bytes; 98.03% used; 225812630 free inodes.

server3 `/tmp`: 84437475328 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84437475328 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637711872 available bytes; 94.11% used; 114350352 free inodes.

server4 `/home`: 105637711872 available bytes; 94.11% used; 114350352 free inodes.

server4 `/data`: 249085845504 available bytes; 96.56% used; 225013669 free inodes.

server4 `/tmp`: 105637711872 available bytes; 94.11% used; 114350352 free inodes.

server4 `/var/tmp`: 105637711872 available bytes; 94.11% used; 114350352 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

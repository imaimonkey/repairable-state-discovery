# V2R cluster inventory

2026-09-25T08:36:00.381258+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318829182976 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318829182976 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318829182976 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318829182976 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 364217532416 available bytes; 98.33% used; 337557080 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22842060800 available bytes; 98.73% used; 110410488 free inodes.

server2 `/home`: 22842060800 available bytes; 98.73% used; 110410488 free inodes.

server2 `/tmp`: 22842060800 available bytes; 98.73% used; 110410488 free inodes.

server2 `/var/tmp`: 22842060800 available bytes; 98.73% used; 110410488 free inodes.

server2 `/mnt/raid5`: 333061038080 available bytes; 97.70% used; 445093989 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436123648 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436123648 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142383333376 available bytes; 98.03% used; 225811580 free inodes.

server3 `/tmp`: 84436123648 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436123648 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633849344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633849344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245036646400 available bytes; 96.61% used; 225003348 free inodes.

server4 `/tmp`: 105633849344 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633849344 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

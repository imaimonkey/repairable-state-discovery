# V2R cluster inventory

2026-09-25T08:35:16.023723+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318829420544 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318829420544 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318829420544 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318829420544 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 364218839040 available bytes; 98.33% used; 337557081 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22842286080 available bytes; 98.73% used; 110410488 free inodes.

server2 `/home`: 22842286080 available bytes; 98.73% used; 110410488 free inodes.

server2 `/tmp`: 22842286080 available bytes; 98.73% used; 110410488 free inodes.

server2 `/var/tmp`: 22842286080 available bytes; 98.73% used; 110410488 free inodes.

server2 `/mnt/raid5`: 333080694784 available bytes; 97.70% used; 445094013 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436131840 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84436131840 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142383955968 available bytes; 98.03% used; 225811599 free inodes.

server3 `/tmp`: 84436131840 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84436131840 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105633861632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633861632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245038714880 available bytes; 96.61% used; 225003437 free inodes.

server4 `/tmp`: 105633861632 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633861632 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.

# V2R cluster inventory

2026-09-25T08:37:32.159549+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318828933120 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318828933120 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318828933120 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318828933120 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 364213260288 available bytes; 98.33% used; 337557069 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22841663488 available bytes; 98.73% used; 110410488 free inodes.

server2 `/home`: 22841663488 available bytes; 98.73% used; 110410488 free inodes.

server2 `/tmp`: 22841663488 available bytes; 98.73% used; 110410488 free inodes.

server2 `/var/tmp`: 22841663488 available bytes; 98.73% used; 110410488 free inodes.

server2 `/mnt/raid5`: 333014114304 available bytes; 97.70% used; 445094067 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84435963904 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84435963904 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142383886336 available bytes; 98.03% used; 225811564 free inodes.

server3 `/tmp`: 84435963904 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84435963904 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633804288 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633804288 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245036400640 available bytes; 96.61% used; 225003134 free inodes.

server4 `/tmp`: 105633804288 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633804288 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
